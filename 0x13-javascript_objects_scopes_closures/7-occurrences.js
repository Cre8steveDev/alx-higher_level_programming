#!/usr/bin/node

// Write a function that returns the number of occurences in a list
// Export

exports.nbOccurences = function (list, searchElement) {
  const newArr = list.filter(item => item === searchElement);
  return newArr.length;
};
