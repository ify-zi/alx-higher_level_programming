#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, function (err, response) {
  console.log('code: ', response.statusCode.toString());
});
