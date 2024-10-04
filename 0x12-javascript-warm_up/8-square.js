#!/usr/bin/node
const arg = process.argv[2];
if (arg !== undefined && !isNaN(parseInt(arg))) {
  for (let y = parseInt(arg); y > 0; y--) {
    console.log('X'.repeat(parseInt(arg)));
  }
} else {
  console.log('Missing size');
}
