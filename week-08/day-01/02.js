'use strict';


var strudents = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

// create a function that counts all the books of an array of students
// not every student has a property called books

// VER 1
// function sumofthebook(object){
//   var x = 0;
//   object.forEach(function(e){
//     x += (e.books || []).length;
//   });
//   return x
// }

// VER 2
// function sumofthebook(object) {
//   return object.reduce(function(sumofbooks, student){
//     sumofbooks += (student.books || []).length;
//     return sumofbooks;
//   }, 0);
// }

function sumofthebook(object) {
  return object.reduce((sumofbooks, student) => sumofbooks += (student.books || []).length, 0);
}

console.log(sumofthebook(strudents));

module.exports = sumofthebook;
