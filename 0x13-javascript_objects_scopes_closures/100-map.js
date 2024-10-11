#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((index, val) => val * index);
console.log(list);
console.log(newList);
