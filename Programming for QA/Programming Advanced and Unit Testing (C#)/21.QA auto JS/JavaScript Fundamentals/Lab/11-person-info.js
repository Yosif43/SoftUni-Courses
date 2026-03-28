function createPersonInfo(firstName, lastName, age) {
    return {
        firstName: firstName,
        lastName: lastName,
        age: age
    };
}

// Example usage:
let person1 = createPersonInfo("Peter", "Pan", "20");
console.log(person1); // Outputs: { firstName: 'Peter', lastName: 'Pan', age: '20' }

let person2 = createPersonInfo("George", "Smith", "18");
console.log(person2); // Outputs: { firstName: 'George', lastName: 'Smith', age: '18' }