#!/usr/bin/node

const secLarge = process.argv.slice(2).map(Number).filter(x => !isNaN(x));

secLarge.sort((a, b) => b - a);

console.log(secLarge.length < 2 ? 0 : secLarge[1]);
