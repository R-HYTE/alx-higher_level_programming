#!/usr/bin/node

/**
 * Count occurrences of a specified element in an array.
 * @param {Array} list - The array to search.
 * @param {*} searchElement - The element to count occurrences of.
 * @returns {number} - The number of occurrences of the specified element.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
