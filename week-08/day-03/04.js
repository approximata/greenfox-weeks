'use strict';
var fs = require('fs');


// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error
function concatContent(filename1, filename2, callback) {
  fs.readFile(filename1, function(err, rawContent1) {
    if (err) {
      return callback(err);
    }
    fs.readFile(filename2, function(err, rawContent2) {
      if (err) {
        return callback(err);
      }
      var contents = String(rawContent1) + String(rawContent2);
      callback(err, contents);
    });
  });
}

function writeOut(err, result) {
  console.log(result);
}


concatContent('apple.txt', 'text02.txt', writeOut);
