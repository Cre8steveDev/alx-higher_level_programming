#!/usr/bin/node

const argvs = process.argv;

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

// Call the Function
add(argvs[2], argvs[3]);
