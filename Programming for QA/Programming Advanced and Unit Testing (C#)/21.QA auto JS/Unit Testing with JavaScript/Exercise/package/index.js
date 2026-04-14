import { derive } from 'calculator';
import { sum } from './calculator.js';

console.log('Hello first package');
console.log(sum(5, 10));

console.log(derive('f(x) = x*x', 3));
