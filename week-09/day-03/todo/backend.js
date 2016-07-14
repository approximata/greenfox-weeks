
'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'start',
  database: 'tododb',
});

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('projecttodo'))

con.connect(function(err){
  if (err) {
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

app.get('/todos', function(req, res){
 con.query('SELECT * FROM todolist', function(err, result){
   if(err){
     console.log(err.toString());
   }
   console.log(result);
   res.json(result);
 })
});

app.get('/todos/:id', function(req, res){
  con.query('SELECT * FROM todolist WHERE id ='
  + Number(req.params.id) + ';', function(err, result){
    console.log(result);
    res.json(result);
  });
});

app.post('/todos', function(req, res){
  con.query('INSERT INTO `todolist` (`text`, `completed`, `destroyed`)' +
  ' VALUES (' + '"' + req.body.text + '"' + ', 0, 0);', function(err, result){
    if(err){
      console.log(err.toString());
    }
    console.log({ id: result.insertId, text: req.body.text });
    res.json({ id: result.insertId, text: req.body.text });
  });
});

app.put('/todos/:id', function(req, res){
  con.query('UPDATE `todolist` SET `text`=' + "'" + req.body.text + "'" + ', `completed`=' + "'" + req.body.completed + "'" + ' WHERE `id`='+ "'" + Number(req.params.id) + "'" +' ;', function(err, result){
    if (err) {
      console.log(err.toString());
      return;
    }
    console.log({ id: result.insertId, text: req.body.text, completed: req.body.completed });
    // errorHandling(res, {id: +req.params.id, text: req.body.text, completed: req.body.completed});
    res.send({ id: result.insertId, text: req.body.text, completed: req.body.completed });
  });
});

app.delete('/todos/:id', function(req, res){
  con.query('UPDATE `todolist` SET `destroyed`=' + "'" + 1 + "'" + ' WHERE `id`='+ "'" + Number(req.params.id) + "'" +' ;', function(err, result){
    if (err) {
      console.log(err.toString());
    }
    console.log(Number(req.params.id + result));
    res.json(result);
  });
});


function errorHandling(res, item) {
 if (item === undefined) {
   res.sendStatus(404);
 } else {
   res.json(item);
 }
}

app.listen(3000);
