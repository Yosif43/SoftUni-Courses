function getNthElements(array, step) {
    let result = [];
    for (let i = 0; i < array.length; i += step) {
        result.push(array[i]);
    }
    return result;
}

// Test examples
console.log(getNthElements(['5', '20', '31', '4', '20'], 2)); // Output: ['5', '31', '20']
console.log(getNthElements(['dsa', 'asd', 'test', 'tset'], 2)); // Output: ['dsa', 'test']
console.log(getNthElements(['1', '2', '3', '4', '5'], 6)); // Output: ['1']