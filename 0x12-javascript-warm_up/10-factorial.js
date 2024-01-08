#!/usr/bin/node

// Defines a recursive function to compute the factorial
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Prints the result of computing the factorial
console.log(factorial(parseInt(process.argv[2])));
