'use strict';
var listofcontent = ['apple', 'banana', 'cat', 'dog'];

var lielemets = document.querySelectorAll('li');

for (var i = 0; i < lielemets.length; i++) {
  (lielemets[i].innerHTML = listofcontent[i]);
}
