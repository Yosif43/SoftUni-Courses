// String declaration (3 literals)
let singleQuoteLiteral = 'First Literal';
let doubleQuotesLiteral = "Second Literal";
let stringInterpolationLiteral = `Third literal`;

// String Concatenation with operator
console.log('Hello ' + 'Ivan');
console.log(10 + '10');

// String concatenation with method
let message = 'Hello ';
console.log(message.concat('Ivan'));

// Index of substring
let text = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Magnam, dolor odio. '
let indexOfDolor = text.indexOf('dolor');
console.log(indexOfDolor);
let lastIndexOfDolor = text.lastIndexOf('dolor');
console.log(lastIndexOfDolor);

// Sunstring
let partOfLorem = text.substring(indexOfDolor, lastIndexOfDolor);
console.log(partOfLorem);

// Replace
let replacedDolor = text.replace('dolor', 'dolar');
console.log(replacedDolor);

// Split string into array
let input = 'Pesho, Gosho, Stamat';
let names = input.split(', ');
console.log(names);

// Includes substring
if (text.includes('Lorem')) {
    console.log('It\'s Lorem');
}

// Repeat a string
let character = '*';
console.log(character.repeat(10));

// Trim string
let nonTrimmedText = '   sometext    ';
console.log(nonTrimmedText.trimStart());
console.log(nonTrimmedText.trimEnd());
console.log(nonTrimmedText.trim());

// Check start and end strings
console.log(text.startsWith('Lorem'));
console.log(text.endsWith('Ipsum'));

// Pad start and pad end
let binaryNumber = 1001;
console.log(binaryNumber.toString().padStart(8, '0'));
console.log('123'.padEnd(8, '*'));

