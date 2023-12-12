#!/usr/bin/node

if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  let repeatedVar = '';
  while (i < process.argv[2]) {
    repeatedVar += 'X';
    i++;
  }
  let z = 0;
  while (z < process.argv[2]) {
    console.log(repeatedVar);
    z++;
  }
}
