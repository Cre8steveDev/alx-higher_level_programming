#!/usr/bin/node

// Write a function that prints the number of arguments already printed and
// the new argument
let count = 0;

exports.logMe = function (item) {
  // Print in stated format
  console.log(`${count}: ${item}`);
  count++;
};
