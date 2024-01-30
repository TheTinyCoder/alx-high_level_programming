#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
request(`https://swapi-api.hbtn.io/api/films/${id}`, (err, res, body) => {
  if (err) { console.error(err); }
  const json = JSON.parse(body);
  console.log(`${json.title}`);
});
