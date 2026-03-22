//Declare Function
function printMultiplicationTableForNumber (number) {
    //обходя всички числа от 1 до 10
    for (let multiplier = 1; multiplier <= 10; multiplier++) {
        //повтаряме: отпечатваме умножението с множителя
        const product = number * multiplier; //резултат от умножение
        console.log(`${number} X ${multiplier} = ${product}`);
    }
}

//Inokation function
printMultiplicationTableForNumber(9);