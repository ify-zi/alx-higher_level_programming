#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
