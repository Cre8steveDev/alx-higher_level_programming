#!/usr/bin/node

// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer
// The first argument is the movie ID
// Use the Star Wars API with endpoint given below

const request = require('request');

const movieId = +process.argv[2];
const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(urlEndpoint, (err, response, body) => {
  if (err) {
    return;
  }
  const movieTitle = JSON.parse(body).title;
  console.log(movieTitle);
});
