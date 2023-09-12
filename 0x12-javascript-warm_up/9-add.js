#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(Number(args[0]), Number(args[1]));
