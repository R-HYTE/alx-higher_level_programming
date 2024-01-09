#!/usr/bin/node

const fs = require('fs');

// Check if the required command-line arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js fileA fileB destinationFile');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

// Read the contents of the first source file
try {
  const content1 = fs.readFileSync(fileA, 'utf8');

  // Read the contents of the second source file
  try {
    const content2 = fs.readFileSync(fileB, 'utf8');

    // Concatenate the contents and write to the destination file
    try {
      fs.writeFileSync(destinationFile, content1 + content2);
      console.log(`Contents of ${fileA} and ${fileB} are concatenated and written to ${destinationFile}.`);
    } catch (writeError) {
      console.error(`Error writing to ${destinationFile}:`, writeError.message);
    }
  } catch (readError2) {
    console.error(`Error reading ${fileB}:`, readError2.message);
  }
} catch (readError1) {
  console.error(`Error reading ${fileA}:`, readError1.message);
  process.exit(1);
}
