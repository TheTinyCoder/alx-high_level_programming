#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const keys = [...new Set(Object.values(dict))];
for (const i in keys) {
  newDict[keys[i]] = Object.entries(dict).filter(([key, value]) => value === keys[i])
    .flat().filter((value, index) => index % 2 === 0);
}
console.log(newDict);
