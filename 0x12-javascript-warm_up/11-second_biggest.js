#!/usr/bin/node

// Get argument from command line
const args = process.argv;

// Print 0 if there's no argument or if just one argument in list
if (args.length < 4) {
  console.log(0);
} else {
  let newArr = args.slice(2);
  newArr = newArr.map(elem => parseInt(elem));

  // Sort the array and take the second to last entry
  newArr = newArr.toSorted();
  console.log(newArr[newArr.length - 2]);
}
