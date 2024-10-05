#!/usr/bin/node
const arg = process.argv[2];
function factorial (x) {
  if (x === 1) {
    return x;
  }
  return (x * factorial(--x));
}
if (arg !== undefined && !isNaN(parseInt(arg))) {
  console.log(factorial(parseInt(arg)));
} else {
  console.log(1);
}
