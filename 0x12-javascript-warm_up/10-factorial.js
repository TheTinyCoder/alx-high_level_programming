#!/usr/bin/node

function factorial (x) {
  let i = 2;
  let result = 1;
  while (i <= x) {
    result = result * i;
    i++;
  }
  return result;
}

if (process.argv.length < 3 || isNaN(process.argv)[2]) {
  console.log(1);
} else { console.log(factorial(process.argv[2])); }
