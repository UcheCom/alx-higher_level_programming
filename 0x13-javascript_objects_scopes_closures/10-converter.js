#!/usr/bin/node

exports.converter = function (base) {
  return function (convert) {
    return convert.toString(base);
  };
};
