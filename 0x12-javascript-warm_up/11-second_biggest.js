#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (node and script name)

function findSecondBiggest (list) {
  let biggest = Number(list[0]);
  let secondBiggest = Number(list[1]);
  for (const n of list) {
    if (biggest < n) {
      secondBiggest = biggest;
      biggest = n;
    }
  }
  return (secondBiggest);
}

if (args.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(args));
}
