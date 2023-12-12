#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { this.width = w; this.height = h; }
  }

  print () {
    let xWidth = '';
    let i = this.width;
    while (i > 0) {
      xWidth += 'X';
      i--;
    }
    let j = this.height;
    while (j > 0) {
      console.log(xWidth);
      j--;
    }
  }
}
module.exports = Rectangle;
