#!/usr/bin/node
// lorem ipsum

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
