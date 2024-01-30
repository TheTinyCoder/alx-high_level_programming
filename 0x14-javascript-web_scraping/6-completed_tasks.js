#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { console.error(err); }
  const data = JSON.parse(body);
  const completedTasks = {};
  for (const task of data) {
    if (task.completed) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId] += 1;
    }
  }
  console.log(completedTasks);
});
