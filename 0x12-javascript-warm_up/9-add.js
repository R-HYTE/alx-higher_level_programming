#!/usr/bin/node

// Defines a function to add two integers
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

// Prints the result of adding the provided integers
console.log(add(process.argv[2], process.argv[3]));
