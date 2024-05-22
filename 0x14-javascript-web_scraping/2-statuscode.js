#!/usr/bin/node

const request = require('request');
const page = process.argv[2];

request(page, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
