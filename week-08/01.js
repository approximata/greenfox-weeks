'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

var string = 'apple';

function countString(str) {
  return str.split('').reduce(function(dic, letter) {
    dic[letter] = (dic[letter] + 1) || 1;
    return dic;
  }, {});
}
console.log(countString(string));

module.exports.countString = countString;
