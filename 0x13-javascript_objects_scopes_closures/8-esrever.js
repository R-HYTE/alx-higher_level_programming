#!/usr/bin/node

/**
 * Reverse the elements of an array.
 * @param {Array} list - The array to be reversed.
 * @returns {Array} - A new array with the reversed elements.
 */
exports.esrever = function (list) {
  return list.reduceRight((reversedArray, current) => {
    reversedArray.push(current);
    return reversedArray;
  }, []);
};
