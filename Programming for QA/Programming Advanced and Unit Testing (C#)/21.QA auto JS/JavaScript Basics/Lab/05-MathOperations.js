//Declare function
function calculate (firstNumber, secondNumber, operator) {
    //operator = '+' -> събиране на firstNumber и secondNumber - OK
    //operator = '-' -> изваждане на firstNumber и secondNumber - OK
    //operator = '*' -> умножение на firstNumber и secondNumber - OK
    //operator = '/' -> деление на firstNumber и secondNumber - OK
    //operator = '%' -> деление с остатък на firstNumber и secondNumber - OK
    //operator = '**' -> повдигане на firstNumber на степен secondNumber

    switch (operator) {
        case '+':
            console.log(firstNumber + secondNumber);
            break;
        case '-':
            console.log(firstNumber - secondNumber);
            break;
        case '*':
            console.log(firstNumber * secondNumber);
            break;
        case '/':
            console.log(firstNumber / secondNumber);
            break;
        case '%':
            console.log(firstNumber % secondNumber);
            break;
        case '**':
            console.log(firstNumber ** secondNumber);
            break;

    }
}

//Invokatin function
calculate(5, 6, '+');
calculate(3, 5.5, '*');