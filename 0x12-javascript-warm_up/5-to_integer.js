#!/usr/bin/node

// Checks if the first argument is a number and prints it in a specific format
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
