
'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var app = express();

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())


var todolist = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
];

app.get('/todos', function(req, res){
  res.json(todolist);
});

app.get('/todos/:id', function(req, res){
  res.json(todolist.filter(function (e){
      return e.id === +req.params.id
    }));
});

app.post('/todos', function(req, res){
  var uniqueid = todolist.length;
  req.body["id"] = uniqueid + 1;
  req.body["completed"] = false;
  todolist.push(req.body);
  res.json(todolist[todolist.length-1]);
});

app.put('/todos/:id', function(req, res){
  var todo = todolist.filter(function (e){
      return e.id === +req.params.id
  })[0];
  todo["completed"] = req.body["completed"];
  todo["text"] = req.body["text"];
  res.json(todo);
});

app.delete('/todos/:id', function(req, res, next){
  var newtodo = todolist.filter(function (e){
      return e.id !== +req.params.id
  });
  var filtered = todolist.filter(function (e){
      return e.id === +req.params.id
  })[0];
  if(filtered === undefined) {
    return next(true);
  }
  filtered["destroyed"] = true;
  res.json(filtered);
  todolist = newtodo;
});

app.use(function(req, res, next) {
  console.log(err.stack);
  res.status(404).send('Sorry cant find that!');
});


app.listen(3000);
