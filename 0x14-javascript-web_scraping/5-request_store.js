#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Write the body response to the specified file
  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error(writeError);
    }
  });
});
