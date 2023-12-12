#!/usr/bin/node

const dict = require('./101-data.js').dict;

const ids = [...new Set(Object.values(dict))];

const newDict = {};

for (let i = 0; i < ids.length; i++) {
  newDict[String(ids[i])] = [];
  for (const j of Object.keys(dict)) {
    if (dict[j] === ids[i]) {
      newDict[ids[i]].push(j);
    }
  }
}

console.log(newDict);
