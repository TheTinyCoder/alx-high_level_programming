#!/usr/bin/node

exports.callMeMoby = function (x, aFunction) {
  let i = 0;
  while (i < x) {
    aFunction.call();
    i++;
  }
};
