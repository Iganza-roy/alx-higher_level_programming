#!/usr/bin/node

const args = parseInt(process.argv[2]);
let i = 0;

if (isNaN(args)) {
	console.log('Missing size');
} else {
	while (i < args) {
		let k = 0;
		let row = '';
		while (k < args ) {
			row += 'X';
			k++;
		}
		console.log(row);
		i++;
	}
}
