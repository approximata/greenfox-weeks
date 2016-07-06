'use strict';
var button = document.querySelector('button');
var lilist  = document.querySelectorAll('li')
 function countList () {
   document.querySelector('.result').textContent = lilist.length
 }
 button.addEventListener('click', countList);
