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
  const promises = [];

  data.characters.forEach((characterUrl) => {
    const promise = new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        const characterData = JSON.parse(body);

        resolve(characterData.name);
      });
    });

    promises.push(promise);
  });

  Promise.all(promises).then((names) => {
    names.forEach((name) => console.log(name));
  }).catch((error) => {
    console.error('An error occurred:', error);
  });
});
