#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body);
    const rest = films.results;
    for (const film of rest) {
      const characters = film.characters;
      for (const chars of characters) {
        if (chars.search('18') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
