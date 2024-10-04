#!/usr/bin/node
const arg = process.argv[2];
if (arg !== undefined && !isNaN(parseInt(arg))) {
  for (let x = parseInt(arg); x > 0; x--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
