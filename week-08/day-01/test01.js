var countString = require('./01');
var test = require('tape');

test('test for apple', function (t) {
  t.deepEqual(countString('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});

test('test for spaces', function (t) {
  t.deepEqual(countString('    '), { ' ': 4 });
  t.end();
});

test('test for empty string', function (t) {
  t.deepEqual(countString(''), {});
  t.end();
});
