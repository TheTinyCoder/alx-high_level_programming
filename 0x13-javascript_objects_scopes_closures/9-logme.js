#!/usr/bin/node
exports.logMe = function logMe (item) {
  logMe.count = logMe.count === undefined ? 0 : ++logMe.count;
  console.log(logMe.count + ': ' + item);
};
