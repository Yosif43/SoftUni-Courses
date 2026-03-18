//Function declaration
function printMonthName (number) {
    //1 -> January
    //2 -> February
    //3 -> March
    //4 -> April
    //5 -> May
    // < 1 или > 12
    //number -> серия от проверки за точни стойности, от които само една е вярна

    switch (number) {
        case 1:
            console.log('January');
            break;
        case 2:
            console.log('February');
            break;
        case 3:
            console.log('March');
            break;
        case 4:
            console.log('April');
            break;
        case 5:
            console.log('May');
            break;
        case 6:
            console.log('June');
            break;
        case 7:
            console.log('July');
            break;
        case 8:
            console.log('August');
            break;
        case 9:
            console.log('September');
            break;
        case 10:
            console.log('October');
            break;
        case 11:
            console.log('November');
            break;
        case 12:
            console.log('December');
            break;
        default:
            //никое условие от горните не е изпълнено
            console.log('Error!');
            break;
    }
}

//Function Invokation
printMonthName(2);
printMonthName(5);
printMonthName(15);
printMonthName(-5);