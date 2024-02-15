#!/usr/bin/node

// Write a class Rectangle that defines a rectangle with other details

class Rectangle {
  // Constructor function of the class
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Create an instance method caled print that prints the rect using X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
