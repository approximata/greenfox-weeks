'use strict';
var firstp = document.querySelector('p');
console.log(firstp.textContent);

var out1 = document.querySelector('.output1');
out1.innerHTML = firstp.textContent
var out2 = document.querySelector('.output2');
out2.innerHTML = firstp.innerHTML
