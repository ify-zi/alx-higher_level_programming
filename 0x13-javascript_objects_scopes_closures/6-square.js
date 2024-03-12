#!/usr/bin/node

const prevSquare = require('./5-square');

module.exports = class Square extends prevSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    super.print(c);
  }
};
