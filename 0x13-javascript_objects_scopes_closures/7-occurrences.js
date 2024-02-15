#!/usr/bin/node

// Write a function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement){
   let newArr = list.filter(item => item === searchElement);
   return newArr.length;
}
