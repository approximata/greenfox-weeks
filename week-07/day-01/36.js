'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah

// var i = 0
var sum = 0
// while(i < ah.length){
//   sum += ah[i]
//   i++
// }
// console.log(sum)

for(var i = 0; i < ah.length; i++){
  sum += ah[i]
}

console.log(sum)
