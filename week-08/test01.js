'use strict';

var tape = require('tape');
var countString1 = require('./01');

tape(function(t) {
  t.deepEqual(countString1.countString('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});
