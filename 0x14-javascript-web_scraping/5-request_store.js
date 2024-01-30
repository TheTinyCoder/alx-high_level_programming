#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { console.error(err); }
  try {
    fs.writeFileSync(process.argv[3], body);
  } catch (err) {
    console.error(err);
  }
});
