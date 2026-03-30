let cars = ['BMW', 'Toyota', 'Audi', 'Mercedes', 'Lada'];
console.log(cars);

// Pop method (mutating method)
let lastCar = cars.pop();
console.log(lastCar);
console.log(cars);

// Push method (mutating method)
cars.push('Trabant');
console.log(cars);

// Shift method (mutating method)
let firstCar = cars.shift();
console.log(firstCar);
console.log(cars);

// unshift method (mutating method)
cars.unshift('Mazda');
console.log(cars);

// Reverse (mutating method)
cars.reverse();
console.log(cars);

// Join (non mutating method)
let carsResult = cars.join(' - ');
console.log(cars);
console.log(carsResult);

// Slice (non mutating method)
let firstCars = cars.slice(0, 3);
console.log(cars);
console.log(firstCars);

// Use slice to create shallow copy of an array
let carsCopy = cars.slice();
console.log(cars);
console.log(carsCopy);
console.log(cars == carsCopy); // equality by refference

// Includes
if (cars.includes('Toyota')) {
    console.log('We have some nice cars here :) ');
}

// IndexOf
let indexOfToyota = cars.indexOf('Toyota');
console.log(indexOfToyota);

// ForEach (non mutating method)
cars.forEach(car => console.log(car));

// Map (non mutating method)
let lowerCaseCars = cars.map(car => car.toLowerCase())
console.log(lowerCaseCars);

// Find (non mutating method)
let carWithT = cars.find(car => car.startsWith('T'));
console.log(carWithT);

// Filter (non mutating method)
let carsWithT = cars.filter(car => car.startsWith('T'));
console.log(carsWithT);
