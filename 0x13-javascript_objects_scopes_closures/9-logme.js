#!/usr/bin/node

let count = 0;

/**
 * Log an item along with a count.
 * @param {*} item - The item to be logged.
 */
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
