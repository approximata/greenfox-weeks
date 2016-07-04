'use strict';

var test = require('tape');
var sumofthebook = require('./02');
var strudents = [
  { name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings'] },
  { name: 'Ryan', age: 11, books: ['The funcdation'] },
  { name: 'Sheela', age: 14 },
  { name: 'Charlee', age: 9, books: [] },
  { name: 'Jessica', age: 12, books: ['Dune'] },
  { name: 'Robert', age: 15 }
];

var strudents1 = [
  { name: 'Steve', age: 12, books:[] },
  { name: 'Ryan', age: 11, books:[] },
  { name: 'Sheela', age: 14 },
  { name: 'Charlee', age: 9, books:[] },
  { name: 'Jessica', age: 12, books:[] },
  { name: 'Robert', age: 15 }
];

var strudents2 = [
  { name: 'Steve', age: 12, },
  { name: 'Ryan', age: 11,},
  { name: 'Sheela', age: 14 },
  { name: 'Charlee', age: 9, },
  { name: 'Jessica', age: 12, },
  { name: 'Robert', age: 15 }
];


test('empty book values', function (t) {
  t.deepEqual(sumofthebook(strudents1), 0);
  t.end();
});

test('no books values', function (t) {
  t.deepEqual(sumofthebook(strudents2), 0);
  t.end();
});

test('filled books values', function (t) {
  t.deepEqual(sumofthebook(strudents), 4);
  t.end();
});
