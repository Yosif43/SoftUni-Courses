//Declare Function
function sumDigits (number) {
    let sum = 0; //сума от цифрите

    //algorithm == съвкупност от стъпки, които решават даден проблем
    //повтаряме -> while
    //1. взимаме последната цифра
    //2. сумираме
    //3. премахваме от числото
    //stop: number <= 0 -> нямаме налични цифри
    //continue repeat: number > 0 -> има налични цифри

    while (number > 0) {
        //number = 37
        //1. взимаме последната цифра
        let lastDigit = number % 10;
        //2. сумираме
        sum += lastDigit;
        //3. премахваме последната цифра от числото
        number = Math.floor(number / 10);
    }

    console.log(sum);
}

//Invokation
sumDigits(376);