#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }

  charPrint (c) {
    const label = 'X';
    let shape = '';
    if (c) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          shape += c;
        }
        console.log(shape);
        shape = '';
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          shape += label;
        }
        console.log(shape);
        shape = '';
      }
    }
  }
};
