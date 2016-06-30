'use strict';
// var asteroid = document.querySelector('div');
//
// console.log(asteroid.classList.value);
//
// console.log('asteroid?', asteroid.classList.contains('asteroid'));
// console.log('planet?', asteroid.classList.contains('planet'));
//
// asteroid.classList.add('new-class');
// asteroid.classList.remove('asteroid');
// console.log('still asteroid?', asteroid.classList.contains('asteroid'));

var pek = document.querySelectorAll('p');

if(pek[2].classList.contains('cat')){
  alert('YEAH CAT!')
};

if(pek[3].classList.value == 'dolphin'){
  pek[0].textContent = 'pear'
}

if(pek[0].classList.value == 'apple'){
  pek[2].textContent = 'dog'
}

pek[0].classList.add('red');

document.querySelector('.balloon').classList.remove('balloon')
