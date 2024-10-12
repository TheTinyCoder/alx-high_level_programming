#!/usr/bin/node
const fs = require('node:fs');
const args = process.argv.slice(2);
const data = fs.readFileSync(args[0]).toString();
const data1 = fs.readFileSync(args[1]).toString();
fs.writeFileSync(args[2], data + data1);
