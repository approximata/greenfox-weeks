'use strict';
var button = document.querySelector('button');

function viewData() {
  var xhr = new XMLHttpRequest();
  var inputvalue = document.querySelector('input').value;
  console.log(inputvalue.split(' ').join('+'));
  xhr.onload = function() {
    document.querySelector('.yodaspeak').textContent = xhr.response;
  };
  xhr.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=' + inputvalue.split(' ').join('+'));
  xhr.setRequestHeader('X-Mashape-Key', 'QtW7DNfmMWmshSuFZ0qezLmYzZ6gp1AGrjajsn1RpghvucNeDW');
  xhr.send();
}

button.addEventListener('click', viewData);
