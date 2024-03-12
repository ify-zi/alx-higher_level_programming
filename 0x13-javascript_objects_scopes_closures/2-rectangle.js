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
};
