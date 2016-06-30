'use strict';

var listofpiccontent = ['./pictures/01.jpg', './pictures/02.jpg', './pictures/03.jpg', './pictures/04.jpg']

var picpreviewed = document.querySelector('.previewed');
var picList = document.querySelector('.tumbpic');
console.log(picList);
// console.log(picpreviewed.getAttribute('src'));
// picpreviewed.setAttribute('src', 'http://deji.chez.com/dessins/pp1.gif');

var rightbutton = document.querySelector('.rightbutton');
var leftbutton = document.querySelector('.leftbutton');
var index = 0;

function createOneTumb(i){
  var newpic = document.createElement('img');
  newpic.src = listofpiccontent[i];
  picList.appendChild(newpic);
}

function createAllTumb(){
    for(var i = 0; i < listofpiccontent.length; i++){
      console.log(listofpiccontent[i]);
      createOneTumb(i);
    }
}

function nextPic() {
  index++;
  if(index >= listofpiccontent.length){
    index = 0;
  }
  console.log(index);
  picpreviewed.setAttribute('src', listofpiccontent[index]);
}
function previousPic() {
  index--;
  if(index <= -1){
    index = listofpiccontent.length - 1;
  }
  console.log(index);
  picpreviewed.setAttribute('src', listofpiccontent[index]);
}
rightbutton.addEventListener('click', nextPic);
leftbutton.addEventListener('click', previousPic);
createAllTumb();
// function indexPic() {
//   listofpiccontent[index].addEventListener('click', )
// }
//
// function changePic() {
//   index =
//   picpreviewed.setAttribute('src', listofpiccontent[index]);
// }
