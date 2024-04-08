#!/usr/bin/node

const args = parseInt(process.argv[2]);
let i = 0;
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  while (i < args) {
    console.log('C is fun');
    i++;
  }
}
