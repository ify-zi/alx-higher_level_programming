#!/usr/bin/node

module.exports = class Rectangle {
  width;
  height;

  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shape += 'X';
      }
      console.log(shape);
      shape = '';
    }
  }
};
