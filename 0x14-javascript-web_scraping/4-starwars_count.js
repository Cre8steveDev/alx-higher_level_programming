#!/usr/bin/node

// Write a script that prints the number of movies where
// the character "Wedge Antilles" is present.
// The first argument is the API URL of the Star wars API:
// https://swapi-api.alx-tools.com/api/films/
// Wedge Antiles' character ID is 18 use this to filter the result

const request = require('request');

const urlEndpoint = process.argv[2];

request.get(urlEndpoint, (err, response, body) => {
  if (err) {
    return;
  }
  const data = JSON.parse(body).results;
  let characterCount = 0;

  for (const movie of data) {
    const isIncluded = movie.characters.includes(
      'https://swapi-api.alx-tools.com/api/people/18/'
    );

    if (isIncluded) {
      characterCount++;
    }
  }

  console.log(characterCount);
});
