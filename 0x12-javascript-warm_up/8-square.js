#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

if (isNaN(Number(args[0]))) {
  console.log('Missing size');
} else {
  const x = Number(args[0]);
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
