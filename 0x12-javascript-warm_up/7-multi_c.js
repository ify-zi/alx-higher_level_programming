#!/usr/bin/node

const val = process.argv[2];

if (!val || isNaN(val)) {
  console.log('Missing number of occurences');
}

for (let i = 0; i < val; i++) {
  console.log('C is fun');
}
