// Declare an array with array literal
let cars = ['BMW', 'Toyota', 'Audi'];

// Declare an empty array and add elements afterwards
let names = [];
names[0] = 'Pesho';
names[1] = 'Gosdho';
console.log(names);

// Hacky way to set length
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.length);
numbers.length = 10;
console.log(numbers);
numbers.length = 3;
console.log(numbers)

// Get first element
let cars2 = ['BMW', 'Toyota', 'Audi', 'Mercedes'];
let firstCar = cars2[0];
console.log(firstCar);
let lastCar = cars2[cars2.length - 1];
console.log(lastCar);

// Get out of range element
let outOfRange = cars2[100];
console.log(outOfRange);

// Array destructuring assignment with reste operator
let [fCar, sCar, ...otherCars] = cars2;
console.log(fCar);
console.log(sCar);
console.log(otherCars);
