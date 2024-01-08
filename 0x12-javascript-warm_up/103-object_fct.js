#!/usr/bin/node

// Defines an object and a function to increment its integer value.
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  myObject.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
