'use strict';
var h1content = document.body.querySelector('h1').textContent;
alert(h1content);
h1content.innerHTML = 'This is your <strong>new content!</strong>';
console.log(h1content.textContent);
var firstpara = document.body.querySelector('p');
console.log(firstpara.textContent);
alert(document.body.querySelector('.other').textContent);
document.body.querySelector('.result').innerHTML = 'lets see what happen';
