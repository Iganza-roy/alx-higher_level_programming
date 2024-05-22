#!/usr/bin/node

const request = require('request');
const epNum = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + epNum, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const responseJ = JSON.parse(body);
    console.log(responseJ.title);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
