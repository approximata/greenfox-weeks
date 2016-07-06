'use strict';
var fs = require('fs');

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

function wordInText(filename, callback) {
  fs.readFile(filename, function(err, rawContent) {
    if (err) {
      return callback(err);
    }
    var number = (String(rawContent).split(/\s/g)).length;
    callback(err, number);
  });
}

function writeOut(err, number) {
  console.log(number);
}


wordInText('apple.txt', writeOut);

wordInText('apple.txt', function(err, count) {
  console.log(count);
});
