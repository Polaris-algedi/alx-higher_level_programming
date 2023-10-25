#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  }

  console.log(completedTasksByUser);
});
