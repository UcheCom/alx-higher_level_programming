#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2]);
const fileB = process.argv[3]);
const fileC = process.argv[4]);

const src1 = fs.readFileSync(fileA).toString();
const src2 = fs.readFileSync(fileB).toString();
const concatSrc = src1 + src2;
fs.writeFileSync(fileC, concatSrc);
