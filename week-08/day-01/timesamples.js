'use strict';

var birthday = new Date(1994, 12, 10);
var copy = new Date();
copy.setTime(birthday.getTime());

console.log(copy);
console.log(birthday);

var end, start;

start = new Date();
for (var i = 0; i < 1000; i++) {
  Math.sqrt(i);
}
end = new Date();

console.log('Operation took ' + (end.getTime() - start.getTime()) + ' msec');

console.log(end.getTime());

console.log(Date.now());

var time = new Date().getTime();
var date = new Date(time);
console.log(date.toString()); // Wed Jan 12 2011 12:42:46 GMT-0800 (PST)
