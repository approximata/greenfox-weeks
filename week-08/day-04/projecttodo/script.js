'use strict';
var button = document.querySelector('.button-text');
var todolist = document.querySelector('.todo-list');
var inputField = document.querySelector('input');

function addHtml(element) {
  var newTodo = document.createElement('div');
  newTodo.classList.add('taskholder');
  newTodo.innerHTML = '<div class="todo-item">' + element.text + '</div> <div class="buttons" id="1"> <button class="delete" type="button"></button> <input class="check" type="checkbox"></input> </div>';
  newTodo.setAttribute('id', element.id);
  todolist.appendChild(newTodo);
  var checked = newTodo.querySelector('.check');
  checked.checked = element.completed;
  inputField.value = '';
}

// function createDelete() {
//
// }

function drawTasks(inputdata) {
  inputdata.forEach(function (element) {
    if ((element.text).length > 0) {
      console.log(element);
      addHtml(element);
    }
  });
}

function addTask() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos/');
  xhr.setRequestHeader('Content-Type', 'application/json');
  var inputFieldValue = inputField.value
  console.log(inputFieldValue);
  xhr.send(JSON.stringify({ "text": inputFieldValue }));
  console.log(JSON.stringify({ "text": inputFieldValue }));
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      addHtml(JSON.parse(xhr.response));
      console.log(JSON.parse(xhr.response));
    }
  };
}

function getToDolList() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var inputdata = JSON.parse(xhr.response);
    drawTasks(inputdata);
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos/');
  xhr.send();
}

getToDolList();

button.addEventListener('click', addTask);
