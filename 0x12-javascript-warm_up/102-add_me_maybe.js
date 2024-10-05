#!/usr/bin/node
exports.addMeMaybe = function (x, func) {
  func(++x);
};
