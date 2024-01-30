#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) { console.error(err); }
  const data = JSON.parse(body);
  let i = 0;
  function task (i) {
    setTimeout(function () {
      request(data.characters[i], (err, res, body) => {
        if (err) { console.error(err); }
        console.log(JSON.parse(body).name);
      });
    }, 500 * i);
  }
  while (i < data.characters.length) {
    task(i);
    i++;
  }
});
