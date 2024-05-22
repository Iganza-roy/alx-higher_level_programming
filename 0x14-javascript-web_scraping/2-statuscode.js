#!/usr/bin/node

const request = require('request');
const page = process.argv[2];

request(page, function (error, response, body) {
  console.log('code: ', response && response.statusCode);
});
