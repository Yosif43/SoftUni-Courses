//Declare Function
function checkAndPrintSum(number) {
    //1. проверка дали цифрите на числото са еднакви
    //true -> ако да еднакви
    //false -> ако са различни
    //2. сумиране на цифрите
    let sum = 0; //сумата от цифрите

    //number = 376
    let digit = number % 10; //произволна цифра от числото, на която трябва да са равни всички останали цифри
    let areTheSame = true;
    //areTheSame = true -> всички цифри са еднакви
    //areTheSame = false -> цифрите са различни

    while (number > 0) {
        //1. взимаме последната цифра
        let lastDigit = number % 10;
        //2. сумирам
        sum += lastDigit;
        //3. проверка дали е еднаква
        if (lastDigit != digit) {
            //имаме цифра в числото, която е различна
            areTheSame = false;
        }
        //4. премахваме последната цифра от числото
        number = Math.floor(number / 10);
    }

    console.log(areTheSame);
    console.log(sum);
}

//Invokation
checkAndPrintSum(1234);