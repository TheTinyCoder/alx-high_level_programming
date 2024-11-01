#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
request(path, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const count = {}; const countDone = {}; const todos = JSON.parse(body);
    [...new Set(todos.map((todo) => todo.userId))].forEach(
      (id) => { count[id] = todos.filter((todo) => todo.userId === id && todo.completed).length; });
    Object.entries(count).filter(([id, value]) => value > 0).forEach(([id, value]) => { countDone[id] = value; });
    console.log(countDone);
  }
});
