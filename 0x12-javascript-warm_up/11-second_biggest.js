#!/usr/bin/node

function compareNumbers (a, b) {
  return a - b;
}

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.sort(compareNumbers);
  console.log(arr[arr.length - 2]);
}
