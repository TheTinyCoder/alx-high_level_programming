#!/usr/bin/node

if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
