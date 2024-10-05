#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  return (a + b);
}
if (args.length >= 2 && !args.some((x) => isNaN(parseInt(x)))) {
  console.log(add(parseInt(args[0]), parseInt(args[1])));
} else {
  console.log('NaN');
}
