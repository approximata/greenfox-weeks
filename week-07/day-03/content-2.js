'use strict';
var lastp = document.querySelector('.dog');
console.log(lastp.textContent);

var allp = document.querySelectorAll('p');
for (var i = 0; i < allp.length; i++) {
  (allp[i].innerHTML = lastp.textContent);
}
