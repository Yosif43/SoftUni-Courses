//Declare Function
function cookNumber (number, firstOp, secondOp, thirdOp, forthOp, fifthOp) {
    //number = '9' -> string -> Ako number е под формата на текст '9' -> number = Number(number)

    //1. върху числото прилагаме firstOp
    number = executeOperation(number, firstOp);
    console.log(number);
    //2. върху числото прилагаме secondOp
    number = executeOperation(number, secondOp);
    console.log(number);
    //3. върху числото прилагаме thirdOp
    number = executeOperation(number, thirdOp);
    console.log(number);
    //4. върху числото прилагаме forthOp
    number = executeOperation(number, forthOp);
    console.log(number);
    //5. върху числото прилагаме fifthOp
    number = executeOperation(number, fifthOp);
    console.log(number);

    //Declare function (helper)
    //изпълни зададената команда върху числото и да върне модифицирано числото спрямо тази команда
    function executeOperation (number, operation) {
        //Chop – divide the number by two
        //dice – square root of a number
        //spice – add 1 to the number
        //bake – multiply number by 3
        //fillet – subtract 20% from the number
        switch (operation) {
            case 'chop':
                number /= 2;
                //number = number / 2;
                break;
            case 'dice':
                number = Math.sqrt(number);
                break;
            case 'spice':
                number += 1;
                //number = number + 1;
                break;
            case 'bake':
                number *= 3;
                //number = number * 3;
                break;
                case 'fillet':
                number = number - 0.2 * number;
                //number =  number * 0.8;
                //number *= 0.8;
                    break;
        }

    return number;
    }
}



//Invokation
cookNumber(9, 'dice', 'spice', 'chop', 'bake', 'fillet');
