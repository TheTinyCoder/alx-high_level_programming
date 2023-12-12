#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { this.width = w; this.height = h; this.xWidth = 'X'; }
  }

  print () {
    let xW = '';
    let i = this.width;
    while (i > 0) {
      xW += this.xWidth;
      i--;
    }
    let j = this.height;
    while (j > 0) {
      console.log(xW);
      j--;
    }
  }

  rotate () {
    const rWidth = this.width;
    this.width = this.height;
    this.height = rWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
