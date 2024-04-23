#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const process = require('process');

const filepath = process.argv[3];
const url = process.argv[2];
let content = '';

request(url, function (_err, _resp, body) {
  content = body.toString();
  fs.writeFile(filepath, content, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
