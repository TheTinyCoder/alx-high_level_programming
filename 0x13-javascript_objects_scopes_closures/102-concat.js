#!/usr/bin/node
const fs = require('node:fs');
const args = process.argv.slice(2);
const data = fs.readFIleSync(args[0], 'utf8');
const data1 = fs.readFIleSync(args[1], 'utf8');
fs.writeFileSync(args[2], data.concat(data1));
