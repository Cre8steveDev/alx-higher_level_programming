#!/usr/bin/node

// Write a script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8

const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Call the writeFile synchronous function
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    return console.log(err);
  }
});
