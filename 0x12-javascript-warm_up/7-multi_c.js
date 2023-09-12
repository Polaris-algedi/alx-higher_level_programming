#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

if (isNaN(Number(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  let x = Number(args[0]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
