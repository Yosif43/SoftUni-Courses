import { expect } from 'chai';
import sum from '../sumOfNumbers.js';

describe('Sum', () => {
    it('Return sum of elements', () => {
        const input = [1, 2, 3];
        const expectedResult = 6;

        const actualResult = sum(input);

        expect(actualResult).to.equal(expectedResult);
    });

    it('Should throw an error when passing non array argument', () => {
        expect(() => sum(4)).to.throw();
    });
});
