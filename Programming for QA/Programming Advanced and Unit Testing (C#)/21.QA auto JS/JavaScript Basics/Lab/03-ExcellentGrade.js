//Declare function
function printGradeType (grade) {
    //grade >= 5.50 -> 'Excellent'
    //grade < 5.50 -> 'Not excellent'
    //1 начин
    /*if (grade >= 5.50) {
        console.log('Excellent')
    } else {
        console.log('Not excellent')
    }*/
    //2 начин
    console.log(grade >= 5.50 ? 'Excellent' : 'Not excellent');
}

//Invokation function
printGradeType(5.50);
printGradeType(4.35);