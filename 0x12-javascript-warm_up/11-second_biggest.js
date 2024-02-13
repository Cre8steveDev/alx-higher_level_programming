#!/usr/bin/node

// Get argument from command line
const args = process.argv;

// Print 0 if there's no argument or if just one argument in list
if (args.length < 4) {
  console.log(0);
} else {
  const sortedArr = args.toSorted();
  console.log(parseInt(sortedArr[args.length - 2]));
}
