#!/usr/bin/node

/**
 * Returns a function that converts a number to a string in the specified base.
 * @param {number} base - The base for conversion.
 * @returns {Function} - A function that converts a number to a string in the specified base.
 */
exports.converter = function (base) {
  return num => num.toString(base);
};
