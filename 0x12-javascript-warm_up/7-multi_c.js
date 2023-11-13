#!/usr/bin/node

const x = process.argv[2];
const num_count = parseInt(x);

if (!isNaN(num_count)) {
  for (let i = 0; i < num_count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
