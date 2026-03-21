//Declare Function
function printAndSum (startNumber, endNumber) {
    //диапазон: [startNumber, endNumber]
    //1. отпечатваме числата в диапазона - OK
    //2. отпечатваме сумата на числата

    //[5; 10]
    //FOR цикъл
    //повтаряме: число + " "
    //начало: startNumber
    //край: endNumber
    //промяна: +1
    let textForPrint = ''; //текст, който ще отпечатваме
    let sum = 0; //сумата на числата
    for (let number = startNumber; number <= endNumber; number++) {
            textForPrint += number + ' ';
            sum += number;
    }

    //textForPrint = '5 6 7 8 9 10 ' -> всички числа в диапазона разделени с интервал
    //имаме излишен интервал след последното число
    console.log(textForPrint.trim());
    //sum -> натрупата сумата от числата
    console.log('Sum: ' + sum);
}

//Invokation function
printAndSum(5, 10);