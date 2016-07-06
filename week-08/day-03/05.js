'use strict';
var fs = require('fs');
// create a function that has 2 paramteres
//  - fileNames: an array of filenames
//  - callback
//
// it should read the files and call the callback with their content concated
// it should have the same order as the filenames
// it should pass the error as a parameter
var filenameses = ['text01.txt', 'text02.txt', 'apple.txt'];

function readContentFromFile(filenames, callback) {
  for (var i = 0; i < filenames.length; i++) {
    fs.readFile(filenames[i], function(err, rawContent) {
      if (err) {
        return callback(err);
      }
      var contents = String(rawContent);
      callback(err, contents);
    });
  }
}

function writeOut(err, content) {
  console.log(content);
}

readContentFromFile(filenameses, writeOut);
