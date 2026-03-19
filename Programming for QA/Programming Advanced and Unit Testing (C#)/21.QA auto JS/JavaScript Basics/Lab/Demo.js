//Declare variables
//let -> променлива, на която ще сменим стойността в последствие
let number = 5; 
number = 10;
//const -> променлива с константна стойност, нямаме право да и сменяме стойностт
const price = 5.60
//price = 2.30; //Error

//Functions
//Declaration -> деклариране на функция
function multiplyBy2 (number) {
    console.log(number * 2);
}
//Invokation -> извикване на фукция
multiplyBy2(3);

//Printing on console
//1. String интерполация -> вмъквам стойности на променливи в даден текст
let age = 25;
let name = 'Desislava';
//Desislava is 25 years old
console.log(`${name} is ${age} years old`);
console.log('This is JS.');
console.log(3 + 4);

//2. Конкатенация -> долепяне на текстове
console.log(name + ' is ' + age + ' years old');

//3. Закръгляне и форматиране
let num = 2.196543;
console.log(Math.round(num, 2)); //закръгляне -> 2.2
console.log(num.toFixed(2)); //форматиране -> 2.20
console.log(Math.floor(num)); //закръгля към най-близкото цяло число надолу -> 2
console.log(Math.ceil(num)); //закръгля към най-близкото цяло число нагоре -> 3


//Variable Scope
//var -> function scope (от началото до края на функция)
function test () {
    var number = 5;
}

//let, const -> block scope (от началото на блока от код {  до края на блока от код})
{
    let a = 5;
    const b = 6;
}
//console.log(a); //Error

//Ternary operator -> заместител на if - else
let universityName = 'Test';
if (universityName === 'Softuni') {
    console.log('Excellent!');
} else {
    console.log('Bad');
}

console.log(universityName === 'Softuni' ? 'Excellent!' : 'Bad');
