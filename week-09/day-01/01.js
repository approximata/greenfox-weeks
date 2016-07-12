'use strict';

var http = require('http');

var server = http.createServer(function(req, res) {
  console.log('request was made: ' + req.url);
  res.writeHead(200, {'Content-Type': 'text/plain'});
  var time = new Date();
  var now = time.getHours() + ':' + time.getMinutes();
  res.end('Hey! How are you?' + req.url + '' + now + req.method);
});


server.listen(3000, '127.0.0.1');
console.log('what is here?');
