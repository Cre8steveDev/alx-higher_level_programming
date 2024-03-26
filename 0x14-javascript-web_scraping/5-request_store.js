#!/usr/bin/node

// Write a script that gets the content of a webpage
// and stores it in a file
// The first argument is the url to request
// the second argument is the file path to store the response
// The file must be utf-8 encoded

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
