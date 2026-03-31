// Declare an object with literal
let cat = {
    name: 'Navcho',
    age: 9,
    isMale: true,
};

// Access property value with dot syntax
console.log(cat.name);

// Access property value with bracket syntax
console.log(cat['age']);

// Add method with method notation syntax
let dog = {
    name: 'Balkan',
    breed: 'Ulichna prevyzhodna',
    makeSound() {
        console.log('Wof wof');
    }
}

dog.makeSound();

// Dynamically add properties and method
dog.age = 10;
dog['isMale'] = true;
dog.eat = function() {
    console.log('Nom nom nom');
}

dog.eat();


// Use static object methods
let dogKeys = Object.keys(dog);
console.log(dog);
console.log(dogKeys);

let dogValues = Object.values(dog);
console.log(dogValues);
dogValues[2](); // Mind blown :) 

let dogEntries = Object.entries(dog);
console.log(dogEntries);
