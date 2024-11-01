#!/usr/bin/node
const request = require('request');
const path = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(path, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    JSON.parse(body).characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (!error) console.log(JSON.parse(body).name);
      });
    });
  }
});
