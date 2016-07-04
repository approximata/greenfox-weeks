'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(x, y) {
  this.x = x;
  this.y = y;
}

Rectangle.prototype.getArea = function() {
  return this.x * this.y;
}

Rectangle.prototype.getCircumference = function() {
  return 2 * (this.x + this.y);
}

var square = new Rectangle(4, 5);
console.log(square.getArea());

console.log(square.getCircumference());
