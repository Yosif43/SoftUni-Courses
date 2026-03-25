function solve(count, input) {
    let firstElements = input.slice(0, count);

    firstElements.reverse();

    let result = firstElements.join(' ');

    console.log(result);
}

solve(3, [10, 20, 30, 40, 50]);
