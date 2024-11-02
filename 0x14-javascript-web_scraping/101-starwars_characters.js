#!/usr/bin/node
const request = require('request');
const path = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
function getName (character) {
  return new Promise((resolve, reject) => {
    request(character, (error, response, body) => {
      if (!error) resolve(JSON.parse(body).name);
    });
  });
}
request(path, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const x of characters) {
      const response = await getName(x); console.log(response);
    }
  }
});
