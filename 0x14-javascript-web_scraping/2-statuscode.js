#!/usr/bin/node

// Write a script that displays the status code of a GET request
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>

const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
