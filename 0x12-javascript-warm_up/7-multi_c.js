#!/usr/bin/node

const x = process.argv[2];
const numcount = parseInt(x);

if (!isNaN(numcount)) {
  for (let i = 0; i < numcount; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
