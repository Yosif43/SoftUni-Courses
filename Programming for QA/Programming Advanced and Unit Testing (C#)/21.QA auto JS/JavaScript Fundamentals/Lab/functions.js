// Declare function declaration
function printMessage(text) {
    console.log(text);
}

// Invoke function
printMessage('Hello World!');

// function declaration
function printHeader() {
    console.log('~~~~~~~~~~~');
    console.log('HEADER');
    console.log('~~~~~~~~~~~');
}

// function expression syntax
let printBody = function () {
    console.log('');
    console.log('DOCUMENT BODY');
    console.log('');
}

// arrow function 
let printFooter = () => {
    console.log('~~~~~~~~~~');
    console.log('FOOTER');
    console.log('~~~~~~~~~~');
}

function printDocument() {
    printHeader();
    printBody();
    printFooter();
}

printDocument();


// Calculator
function calc(a, b) {
    return a + b;
}

let result = calc(4, 21);
console.log(result);

// Arrow function expression body
let multiply = (a, b) => a * b;
console.log(multiply(10, 20));

// Pass function as argument
function execute(operation, oprands) {
    let result = operation(oprands[0], oprands[1]);

    console.log(result);
}

execute(multiply, [5, 10]);

// Return function from function
function buildOperation(operationName) {
    if (operationName == 'sum') {
        return calc;
    }

    if (operationName == 'divide') {
        return (a, b) => a / b;
    }
}

let divide = buildOperation('divide');
console.log(divide(10, 2));
