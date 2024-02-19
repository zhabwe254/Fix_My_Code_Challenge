#!/usr/bin/node
/*
    Print a square with the character #

    The size of the square must be the first argument 
    of the program.
*/

// Check if the size argument is provided
if (process.argv.length !== 3) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1);
}

// Get the size of the square from the command line argument
const size = parseInt(process.argv[2]);

// Check if the size is a valid positive integer
if (isNaN(size) || size < 1) {
    process.stderr.write("Invalid size\n");
    process.exit(1);
}

// Print the square
for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
        row += '#';
    }
    console.log(row);
}
