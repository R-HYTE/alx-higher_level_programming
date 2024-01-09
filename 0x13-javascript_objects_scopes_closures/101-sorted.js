#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = Object.entries(dict).reduce((result, [key, value]) => {
  result[value] = result[value] || [];
  result[value].push(key);
  return result;
}, {});

console.log(newDict);
