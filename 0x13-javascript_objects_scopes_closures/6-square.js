#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      this.print(c);
    }
  }
}

module.exports = Square;
