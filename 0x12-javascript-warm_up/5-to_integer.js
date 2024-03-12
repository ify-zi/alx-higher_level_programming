#!/usr/bin/node

const num = process.argv[2];
const numc = parseInt(num, 10);

if (process.argv[2] === undefined || isNaN(numc)) {
  console.log('My number: Not a number');
} else {
  console.log('My number: ' + numc);
}
