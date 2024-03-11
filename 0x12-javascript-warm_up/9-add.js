#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];
const aInt = parseInt(a, 10);
const bInt = parseInt(b, 10);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(aInt, bInt);
