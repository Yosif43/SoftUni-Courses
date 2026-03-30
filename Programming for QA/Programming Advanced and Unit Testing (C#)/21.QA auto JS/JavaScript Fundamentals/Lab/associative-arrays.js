// Declare object associative array

let phonebook = {
    'Ivan Ivanov': '+123123123',
    'Petar Ivanov': '+1212423',
    'Grigor Ivanov': '+12543423',
};

// Declare object with dynamic key
let dailySpecial = 'bananas';
let storageStock = {
    'oranges': 10,
    'apples': 20,
    [dailySpecial]: 30,
    'carrots': 0,
    'pears': 14,
};

// Access dynamic property
console.log(storageStock[dailySpecial]);

// For in
for (let key in storageStock) {
    console.log(`${key} -> ${storageStock[key]}`);
}

// Check if value exists
if (storageStock['apples']) {
    console.log('There are aples yes');
}

// CHeck if key exists (property name)
if (storageStock.hasOwnProperty('carrots')) {
    console.log('There is carrot registered');
}

// Remove property
delete storageStock.carrots;
console.log(storageStock);

// Object destructuring assignment
let { apples, oranges, ...others } = storageStock;
console.log(apples);
console.log(oranges);
console.log(others);
