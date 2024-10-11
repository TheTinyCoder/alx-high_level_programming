#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let x = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[x] = list[i];
    x++;
  }
  return reversedList;
};
