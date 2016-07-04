'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)
//
// every car should have an id property (a number), that is
// unique for all the cars, staeting form 0
//
// Methods:
// enter(enterDate)
//  - it should store the date of entering
//
// getEnterDate()
//  - it should return the date of the last entering
//
// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)
//
// getStats()
//  - it should give back a string like:
//    "Type: volvo, Color: red, Balance: 500"
//
//

function Car(typeofcar, color, balance) {
  this.typeofcar = typeofcar;
  this.color = color;
  this.balance = balance;
  this.id = 0;
  this.enters = [];
}

Car.prototype.enter = function(enterDate) {
  var enterD = new Date(enterDate);
  this.enters.push(enterD.getTime());
  return this.enters;
};

Car.prototype.getEnterDate = function() {
  var lastenter = new Date(this.enters[(this.enters).length - 1]);
  return lastenter.toString();
};

Car.prototype.leave = function(price) {
  this.balance -= price;
  return this.balance;
};

Car.prototype.getStats = function() {
  return 'Type: ' + this.typeofcar + ' color: ' + this.color + ' balance: ' + this.balance
}

var myauto = new Car('trabant','red','120');
console.log(myauto.enter('Dec 25, 1995'));
console.log(myauto.enter('Dec 25, 2014'));
myauto.leave(40);
console.log(myauto.getStats());
console.log(myauto.getEnterDate());
console.log(myauto.enters);


// Create a CarPark constructor
// it should take 2 parameters
//  - income: the initial credits as a number (eg: 4000)
//  - startTime: the current date
//
// The parking fee: 40 per hours (only every whole hour)
//
// Methods:
// carEnter(car)
//  - It should add a car to the garage and add its stored startTime
//
// carLeave(id)
//  - It should remove the car with the given id and it should charge from its balance
//
// elapseTime(hours)
//  - It should increment the time with the hours
//
// Optional Methods:
//
// getStats()
//  - It should return a string like:
//    "Cars: 4, Time: 1234423453, Income: 1400"
//
// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours
