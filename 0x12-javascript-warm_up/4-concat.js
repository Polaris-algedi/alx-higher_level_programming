#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

console.log(`${args[0]} is ${args[1]}`);
