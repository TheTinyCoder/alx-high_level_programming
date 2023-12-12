#!/usr/bin/node

const fs = require('fs');

const files = process.argv.slice(2);

const fOne = fs.readFileSync(files[0]).toString();
const fTwo = fs.readFileSync(files[1]).toString();

fs.writeFileSync(files[2], fOne + fTwo);
