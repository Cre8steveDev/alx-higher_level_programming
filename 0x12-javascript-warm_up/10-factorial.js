#!/usr/bin/node

// Get the Variable from command line
const arg = process.argv[2];

// Define Function
function factorial (num) {
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

// Convert number to valid integer
const convertedNum = parseInt(arg);

if (!convertedNum) {
  console.log(1);
} else {
  console.log(factorial(convertedNum));
}
