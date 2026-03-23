//Declare Function
function reverseTexts (firstSymbol, secondSymbol, thirdSymbol) {
    //firstSymbol = 'D'
    //secondSymbol = 'R'
    //thirdSymbol = 'Y'
    //result = 'Y R D'
    const resultText = thirdSymbol + ' ' + secondSymbol + ' ' + firstSymbol;
    console.log(resultText);
}

//Invokation
reverseTexts('A', 'B', 'C');