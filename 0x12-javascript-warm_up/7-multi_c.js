#!/usr/bin/node

const args = process.argv[2];

const num = parseInt(args);

if (!args) {
  console.log('Missing number of occurrences');
} else {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
