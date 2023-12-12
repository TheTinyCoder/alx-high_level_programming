#!/usr/bin/node

const SquareOne = require('./5-square.js');
class Square extends SquareOne {
  // constructor (size) { super(size); }
  charPrint (c) {
    if (c) { super.xWidth = c; }
    super.print();
  }
}
module.exports = Square;
