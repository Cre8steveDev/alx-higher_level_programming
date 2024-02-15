#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of
// 5-square.js

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
