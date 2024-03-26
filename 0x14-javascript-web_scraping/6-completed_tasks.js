#!/usr/bin/node

// Write a script that computes the number of tasks
// Completed by user id.
// The first argument is the API URL:
// https://jsonplaceholder.typicode.com/todos
// Only print users with completed task

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  const data = JSON.parse(body);
  const todoObject = {};

  data.map((datam) => {
    if (!todoObject[datam.userId]) {
      todoObject[datam.userId] = 0;
    }

    todoObject[datam.userId] += datam.completed === true ? 1 : 0;
    return datam;
  });

  console.log(todoObject);
});
