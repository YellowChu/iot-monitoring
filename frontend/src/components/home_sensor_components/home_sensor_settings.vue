<template>
<div>
    <div class="home-sensor-command">
        <div class="row">
            <div class="col">
                <form class="sensor-form">
                    <div class="mb-3">
                        <label for="exampleFormControlSelect1">Change SF</label>
                        <select class="form-control" id="exampleFormControlSelect1">
                            <option>SF7</option>
                            <option>SF8</option>
                            <option>SF9</option>
                            <option>SF10</option>
                            <option>SF11</option>
                            <option>SF12</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="exampleColorInput" class="form-label">Change color</label>
                        <input type="color" class="form-control" id="exampleColorInput" value="#563d7c" title="Choose your color">
                    </div>
                    <div class="mb-3">
                        <button class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
            <div class="col">
                <div class="jumbotron jumbotron-fluid bg-light">
                    <div class="container">
                        <h4 class="display-4">Fluid jumbotron</h4>
                        <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
                    </div>
                </div>
            </div>
        </div>  
    </div>
</div>
</template>

<style>
.home-sensor-command {
    margin-top: 1rem;
}
.sensor-form {
  text-align: left;

}
</style>