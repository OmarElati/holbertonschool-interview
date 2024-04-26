#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2] + '/';
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

// Make API request, set async to allow await promise
request(apiUrl + movieId, async function (error, response, body) {
  if (error) return console.error(error);

  // Find URLs of each character in the movie as a list object
  const characterUrls = JSON.parse(body).characters;

  // Use URL list to fetch character pages and print names
  for (const characterUrl of characterUrls) {
    await new Promise(function (resolve, reject) {
      request(characterUrl, function (error, response, body) {
        if (error) return console.error(error);

        // Find each character's name and print
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
