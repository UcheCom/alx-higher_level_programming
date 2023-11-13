#!/usr/bin/node

const parsedNum = parseInt(process.argv[2]);

if (!isNaN(parsedNum)) {
  console.log('My number: ' + parsedNum);
} else {
  console.log('Not a number');
}
