#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

function findSecondLargest (args) {
  if (args.length <= 1) {
    return 0;
  }

  const numbers = args.map(Number); // Convert arguments to an array of numbers
  // Sort the array of numbers in descending order
  const sortedNumbers = numbers.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];
  return secondLargest;
}

console.log(findSecondLargest(args));
