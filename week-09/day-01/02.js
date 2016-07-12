'use strict';

var express = require('express');

var app = express();
var time = new Date();
var now = time.getHours() + ':' + time.getMinutes();

app.get('/:foo', function(req, res){
  res.send('this is the new page ' + req.params.foo + ' ' + now + ' ' + req.method);
});

app.listen(3000);
