function rotateArray(arr, rotations) {
    const n = arr.length;
    rotations = rotations % n;
    const result = arr.slice(rotations).concat(arr.slice(0, rotations));
    console.log(result.join(" "));
}

function rotateArrayy(array, countRotations) {
    for (let count = 1; count <= countRotations; count++) {
        let firstElement = array.shift()
        array.push(firstElement)
    }
    console.log(array.join(" "));
}

// Test examples
rotateArrayy([51, 47, 32, 61, 21], 2); // Output: 32 61 21 51 47
rotateArrayy([32, 21, 61, 1], 4); // Output: 32 21 61 1
rotateArrayy([2, 4, 15, 31], 5); // Output: 4 15 31 2