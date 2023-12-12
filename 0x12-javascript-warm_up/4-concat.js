#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('undefined is undefined');
} else {
  process.argv.slice(2).forEach((element, index, array) => { if (index % 2 === 0) console.log(`${element} is ${array[index + 1]}`); });
}
