#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
const taskComptd = {};

request(url, function (error, response, body) {
  if (error === null) {
    const jsons = JSON.parse(body);

    for (const json of jsons) {
      if (json.userId in taskComptd) {
        if (json.completed) {
          taskComptd[json.userId] += 1;
        }
      } else {
        if (json.completed) {
          taskComptd[json.userId] = 1;
        }
      }
    }
    console.log(taskComptd);
  }
});
