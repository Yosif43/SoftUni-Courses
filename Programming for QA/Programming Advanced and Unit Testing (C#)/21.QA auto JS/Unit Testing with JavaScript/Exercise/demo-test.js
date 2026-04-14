function sortArr(arr) {
    arr.sort((a, b) => a - b);
}

// Custom TEST
function sortArrTest() {
    // Arrange
    let inputValue = [9, 3, 10, 6];
    let expectedValue = [3, 6, 9, 10];

    // Act
    sortArr(inputValue);

    // Assert
    let actualResult = JSON.stringify(inputValue);
    let expectedResult = JSON.stringify(expectedValue);
    if (actualResult !== expectedResult) {
        throw new Error(`Expected ${actualResult} to be equal to ${expectedResult}`);
    } 

    console.log(`TEST Passed!`);
}

sortArrTest();


