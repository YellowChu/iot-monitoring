from base64 import b64decode
from struct import unpack

from django.contrib.postgres.fields import ArrayField
from django.db import models

'''
TTN payload example:
{
    'end_device_ids': {
        'device_id': 'lopy4-otaa',
        'application_ids': {
            'application_id': 'bp-lora-nguyen'
        }, 
        'dev_eui': '70B3D5499E3B06C1',
        'join_eui': '0000000000000000',
        'dev_addr': '260B8908'
    },
    'correlation_ids': [
        'as:up:01FQ4B3GXMFN34CV9HXRR74CBM',
        'gs:conn:01FQ20GXKCDHAWB00T9NZRPBHG',
        'gs:up:host:01FQ20GXKREN1HZ9QT7FS36F7K',
        'gs:uplink:01FQ4B3GQ5D9NQ9TFZEG93FJ2A',
        'ns:uplink:01FQ4B3GQ8DCH9KDTY7HT73PE3',
        'rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01FQ4B3GQ780ZEN0SHME3J4JGT',
        'rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01FQ4B3GXKK4T06QZJT5MBC9RK'
    ],
    'received_at': '2021-12-17T14:00:32.948967098Z',
    'uplink_message': {
        'session_key_id': 'AX3HtdLk7NjPO+xyro+VKw==',
        'f_port': 2,
        'f_cnt': 10,
        'frm_payload': 'cstLtgAMxEcMNcdBkyKWQA==',
        'rx_metadata': [{
            'gateway_ids': {
                'gateway_id': 'ttig-brno-bystrc',
                'eui': '58A0CBFFFE802A45'
            },
            'time': '2021-12-17T14:00:32.620971918Z',
            'timestamp': 893350363,
            'rssi': -48,
            'channel_rssi': -48,
            'snr': 10.5,
            'uplink_token': 'Ch4KHAoQdHRpZy1icm5vLWJ5c3RyYxIIWKDL//6AKkUQ2+P9qQMaDAiAsPKNBhCd0MnhAiD4/tL+/+MRKgwIgLDyjQYQjo+NqAI='
        }],
        'settings': {
            'data_rate': {
                'lora': {
                    'bandwidth': 125000, 'spreading_factor': 7
                }
            },
            'coding_rate':
            '4/5',
            'frequency': '867100000',
            'timestamp': 893350363,
            'time': '2021-12-17T14:00:32.620971918Z'
        },
        'received_at': '2021-12-17T14:00:32.744138949Z',
        'consumed_airtime': '0.066816s',
        'network_ids': {
            'net_id': '000013',
            'tenant_id': 'ttn',
            'cluster_id': 'ttn-eu1'
        }
    }
}
'''

class Uplink(models.Model):
    payload = models.CharField(max_length=256)
    received_at = models.DateTimeField(default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    spreading_factor = models.PositiveSmallIntegerField(null=True, default=None)
    consumed_airtime = models.DecimalField(max_digits=15, decimal_places=9, null=True, default=None)

    class Meta:
        ordering = ["-received_at"] 


class Gateway(models.Model):
    gateway_id = models.CharField(max_length=128)
    gateway_eui = models.CharField(max_length=128)

    uplinks = models.ManyToManyField(Uplink, blank=True)


class RoomSensor(models.Model):
    device_id = models.CharField(max_length=256, default="", unique=True)
    device_name = models.CharField(max_length=256, default="", blank=True)
    device_description = models.TextField(blank=True)

    uplinks = models.ManyToManyField(Uplink, blank=True)
    displayed_uplinks_number = models.PositiveIntegerField(null=True)
    display_temperature = models.BooleanField(default=True)
    display_pressure = models.BooleanField(default=False)

    def __str__(self):
        return self.device_id

    def parse_uplink_payload(self, payload):
        payload_hexed = b64decode(payload).hex()
        pressure = unpack("f", bytes.fromhex(payload_hexed[8:16]))[0]
        temperature = unpack("f", bytes.fromhex(payload_hexed[16:24]))[0]
        battery = unpack("f", bytes.fromhex(payload_hexed[24:32]))[0]

        return pressure, temperature, battery


class MailboxNotifier(models.Model):
    device_id = models.CharField(max_length=256, default="", unique=True)
    device_name = models.CharField(max_length=256, default="", blank=True)
    device_description = models.TextField(blank=True)

    is_mail = models.BooleanField(default=False)
    number_of_mails = models.PositiveSmallIntegerField(blank=True, default= 0)

    should_notify = models.BooleanField(default=False)
    emails = ArrayField(
            models.CharField(max_length=64),
            blank=True,
            default=list,
        )

    def __str__(self):
        return self.device_id
    
    def clear_mailbox(self):
        self.is_mail = False
        self.number_of_mails = 0
        

class DailyDownlinksCount(models.Model):
    DAILY_LIMIT = 10

    date = models.DateTimeField(auto_now_add=True)
    downlink_count = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    
    room_sensor = models.ForeignKey(RoomSensor, related_name="daily_downlink_count", null=True, on_delete=models.CASCADE)
