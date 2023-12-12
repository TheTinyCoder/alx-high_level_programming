#!/usr/bin/node

exports.nbOccurences = function (list, element) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === element) {
      count += 1;
    }
  }
  return count;
};
