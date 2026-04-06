function oddAndEvenSum(number) {
    const digits = number.toString();
    let oddSum = 0;
    let evenSum = 0;

    for (let i = 0; i < digits.length; i++) {
        const digit = parseInt(digits[i]);
        if (digit % 2 === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`;
}

console.log(oddAndEvenSum(1000435));
console.log(oddAndEvenSum(3495892137259234));