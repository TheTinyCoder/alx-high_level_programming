#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { console.error(err); }
  const json = JSON.parse(body);
  let count = 0;
  json.results.forEach(value => {
    value.characters.forEach(character => {
      if (character.search('18') > 0) { count += 1; }
    });
  });
  console.log(count);
});
