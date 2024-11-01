#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
request(path, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log(
      JSON.parse(body).results.filter(
        (film) => film.characters.some((c) => c.endsWith('18/'))).length);
  }
});
