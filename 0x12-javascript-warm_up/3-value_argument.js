#!/usr/bin/node

const args = process.argv;
let count = 0;

function countArgs (args) {
  for (const i in args) {
    count = i + 1;
  }
}

countArgs(args);

if (count < 3) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
