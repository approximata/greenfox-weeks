'use strict';
var fs = require('fs');

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error


function letterInText(filename, letter, callback) {
  fs.readFile(filename, function(err, rawContent) {
    if (err) {
      return callback(err);
    }
    var letters = (String(rawContent).split(''));
    var number = 0;
    for (var i = 0; i < letters.length; i++) {
      if (letters[i] === letter) {
        number++;
      }
    }
    callback(err, number);
  });
}

function writeOut(err, number) {
  console.log(number);
}

letterInText('apple.txt', 'e', writeOut);

// letterInText('apple.txt', function(err, count) {
//   console.log(count);
// });
