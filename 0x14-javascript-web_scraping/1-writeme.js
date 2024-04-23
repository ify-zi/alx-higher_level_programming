#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];
const txt = process.argv[3];

fs.writeFile(filePath, txt, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
