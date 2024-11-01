#!/usr/bin/node
const fs = require('node:fs');
const request = require('request');
const path = process.argv[2];
request(path, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, { encoding: 'utf8', flag: 'w+' }, (err) => {
      if (err) console.error(err);
    });
  }
});
