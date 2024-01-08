#!/usr/bin/node

// Searches the second biggest integer in the list of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number);
  const sortedList = list.sort((a, b) => b - a);
  console.log(sortedList[1]);
}
