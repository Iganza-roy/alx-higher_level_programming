#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charId = '18';
let cnt = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const k = JSON.parse(body);
    k.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          cnt += 1;
        }
      });
    });
    console.log(cnt);
  }
});
