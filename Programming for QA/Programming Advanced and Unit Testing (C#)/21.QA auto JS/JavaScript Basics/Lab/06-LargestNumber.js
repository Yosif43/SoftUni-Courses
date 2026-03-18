//Declare function
function printLargestNumber (n1, n2, n3) {
    const largestNumber = Math.max(n1, n2, n3); //най-голямото число
    console.log(`The largest number is ${largestNumber}.`);
}

//Invokation function
printLargestNumber(5, -3, 16);
printLargestNumber(-3, -5, -22.5);