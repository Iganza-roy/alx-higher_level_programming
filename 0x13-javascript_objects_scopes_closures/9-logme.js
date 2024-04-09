#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof exports.logMe.count === 'undefined') {
    exports.logMe.count = 0;
  }

  console.log(`${exports.logMe.count}: ${item}`);

  exports.logMe.count++;
};
