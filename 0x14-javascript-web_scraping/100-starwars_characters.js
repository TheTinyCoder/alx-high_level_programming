#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) { console.error(err); }
  const data = JSON.parse(body);
  data.characters.forEach(value => request(value, (err, res, body) => { if (err) { console.error(err); } console.log(JSON.parse(body).name); }));
});
