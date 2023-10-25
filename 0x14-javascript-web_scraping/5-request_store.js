#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('An error occurred while writing to file:', err);
    }
    // console.log('Webpage content stored successfully');
  });
});
