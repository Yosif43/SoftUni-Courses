import { assert, expect } from 'chai'
import * as calculator from '../calculator.js';

describe('Calculator sum', () => {
    it('Should return positive number when adding two positive numbers', () => {
        // Arrange
        let firstNumber = 1;
        let secondNumber = 2;
        let expectedResult = 3;

        // Act
        let actualResult = calculator.sum(firstNumber, secondNumber);

        // Assert
        expect(actualResult).to.equal(expectedResult);
    });

    it('Should return negative number', () => {
        let result = calculator.sum(-1, -10);

        expect(result).to.be.below(0);
    });
});

describe('Calculator subtract', () => {
    it('Should return zero when subtracting same positive numbers', () => {
        const result = calculator.subtract(5, 5);

        expect(result).to.equal(0);
    });
});
