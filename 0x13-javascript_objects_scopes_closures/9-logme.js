#!/usr/bin/node

// Write a function that prints the number of arguments already printed and
// the new argument

exports.logMe = function (item) {
  logMe.count = (logMe.count || 0);

  console.log(`${logMe.count}: ${item}`)
  logMe.count++;
}
