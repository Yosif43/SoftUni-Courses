function SortedNumbers(numbers) {

    let sortedNumbers = numbers.sort((e1, e2) => {
        return e1 - e2
    });
    result = [];
    const length = numbers.length;
    for (let i = 0; i <= length - 1; i++) {
        if (i % 2 == 0) {
            result.push(sortedNumbers.shift());

        } else {
            result.push(sortedNumbers.pop())
        }
    }
    return result
}

console.log(SortedNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));