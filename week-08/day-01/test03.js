'use strict';
var Rectangle= require('./03');
var test = require('tape');

test('basic functions', function(t) {
  var rect = new Rectangle(5, 10);
  t.deepEqual(rect.getArea(), 50);
  t.deepEqual(rect.getCircumference(), 30);
  t.end();
})

test('object created', function(t) {
  var rect = new Rectangle(1, 1);
  t.ok(rect, 'object created');
  t.end();
})
