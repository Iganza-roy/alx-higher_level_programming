#!/usr/bin/node

exports.converter = function (base) {
  function converter (n) {
    return n.toString(base);
  }
  return converter;
};
