#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length >= 2) {
  args.sort((a, b) => b - a);
  console.log(args[1]);
} else {
  console.log(0);
}
