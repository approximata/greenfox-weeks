function getToDolList() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var inputdata = JSON.parse(xhr.response);
    drawTasks(inputdata);
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos/');
  xhr.send();
}

function drawAllTodosWithCheck(todos) {
  

}
