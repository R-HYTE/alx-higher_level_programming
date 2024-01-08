#!/usr/bin/node

const add = (a, b) => a + b;

// Make the function visible from outside by exporting it
module.exports = {
  add: add
};
