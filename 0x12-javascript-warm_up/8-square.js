#!/usr/bin/node

const size = process.argv[2];
const sizet = parseInt(size, 10);
const label = 'X';
let shape = '';

if (!size || isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < sizet; i++) {
  for (let j = 0; j < sizet; j++) {
    shape += label;
  }
  console.log(shape);
  shape = '';
}
