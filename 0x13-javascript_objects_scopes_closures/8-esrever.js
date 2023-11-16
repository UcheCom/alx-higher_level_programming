#!/usr/bin/node

exports.esrever = function (list) {
  const reverList = [];
  const n = list.length;

  for (let i = n - 1; i >= 0; i--) {
    reverList[n - i - 1] = list[i];
  }

  return reverList;
};
