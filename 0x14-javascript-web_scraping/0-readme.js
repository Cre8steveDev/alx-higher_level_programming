#!/usr/bin/node

// Write a script that reads and prints the content of a file
// First argument is the file path
// The content of the file must be read in utf-8
// If an error occurs during the reading, print the error object

const fs = require('fs');

const filePath = process.argv[2];

// Read file content with the fs Read file function
fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  // Check if error occured
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
