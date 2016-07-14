'use strict';
var button = document.querySelector('.button-text');
var todolist = document.querySelector('.todo-list');
var inputField = document.querySelector('input');
var url = 'http://localhost:3000/todos/';
var checktrue = 1;


function addHtml(element) {
  var newTodo = document.createElement('div');
  newTodo.classList.add('taskholder');
  newTodo.innerHTML = '<div class="todo-item">' + element.text + '</div> <div class="buttons"> <button class="delete" type="button" id=' + 'd' + element.id + '></button> <input class="check" type="checkbox" id=' + 'c' + element.id + '></input> </div>';
  newTodo.setAttribute('id', 'task' + element.id);
  todolist.appendChild(newTodo);
  newTodo.querySelector('#d' + element.id).addEventListener('click', deleteTask);
  newTodo.querySelector('#c' + element.id).addEventListener('click', chkTask);
  var checked = newTodo.querySelector('.check');
  var checkdb = false;
  if (element.completed === 1) {
    checkdb = true;
  } else if (element.completed === 0) {
    checkdb = false;
  }
  checked.checked = checkdb;
  inputField.value = '';
}

function deleteTask(event) {
  var xhr = new XMLHttpRequest();
  var targetId = event.target.id;
  console.log(targetId);
  var serverId = targetId.slice(1);
  console.log(serverId);
  xhr.open('DELETE', url + serverId, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      todolist.removeChild(document.querySelector('#task' + serverId));
    }
  }
  xhr.send(null);
}

function xhrRequest(method, urlr, data, type, cb) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, urlr, true);
  xhr.setRequestHeader(type, 'application/json');
  xhr.send(data);
  xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
      cb(JSON.parse(xhr.response));
      console.log(JSON.parse(xhr.response));
    }
  };
}

function trueFalseSql(input) {
  if (input === true) {
    return 1;
  } else if (input === false) {
    return 0;
  }
}

function chkTask(event) {
  // var xhr = new XMLHttpRequest();
  var id = event.target.getAttribute('id').slice(1);
  var texttask = document.querySelector('#task' + id).textContent;
  var checker = trueFalseSql(document.querySelector('#c' + id).checked);
  console.log(id);
  console.log(texttask);
  console.log(checker);
  var method = 'PUT';
  var urlr = url + id;
  var type = 'Content-Type';
  var data = JSON.stringify({ text: texttask, completed: checker })
  console.log(data);
  xhrRequest(method, urlr, data, type, function(response){
    console.log('kakikaki');
    console.log(response);
  });
  // xhr.open('PUT', url + id, true);
  // xhr.setRequestHeader('Content-Type', 'application/json');
  // xhr.onload = function() {
  //   if (xhr.readyState === 4) {
  //     document.querySelector('#c' + id).classList.add('checked');
  //   }
  // };
}

function drawTasks(inputdata) {
  inputdata.forEach(function (element) {
    if ((element.text).length > 0 && element.destroyed === 0) {
      console.log(element);
      addHtml(element);
    }
  });
}

function addTask() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);
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
  xhr.open('GET', url);
  xhr.send();
}

getToDolList();

button.addEventListener('click', addTask);
