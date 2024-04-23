#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, msg) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(msg);
  }
});
