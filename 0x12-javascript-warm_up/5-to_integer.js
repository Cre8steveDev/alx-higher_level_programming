#!/usr/bin/node

const args = process.argv[2];

if (parseInt(args, 10).toString() === args) {
  console.log(`My number: ${parseInt(args, 10)}`);
} else {
  console.log('Not a number');
}
