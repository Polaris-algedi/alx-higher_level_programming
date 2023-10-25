#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const data = JSON.parse(body);

  data.characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
