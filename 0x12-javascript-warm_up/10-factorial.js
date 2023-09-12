#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(args[0])));
