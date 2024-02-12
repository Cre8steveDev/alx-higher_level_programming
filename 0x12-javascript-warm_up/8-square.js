#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined || !(parseInt(arg, 10).toString() === arg)) {
  console.log('Missing size');
} else {
  const num = parseInt(arg, 10);
  for (let i = 0; i < num; i++) {
    const text = 'X'.repeat(num);
    console.log(text);
  }
}
