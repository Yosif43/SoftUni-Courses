//Declare function
function isYearLeap(year) {
    //начин 1 -> if else 
    //високосна -> yes
    /*if ((year % 4 === 0 && year % 100 != 0) || (year % 400 === 0)) {
        console.log('yes');
    } else {
        //не е високосна -> no
        console.log('no');
    }*/
    //начин 2 -> тернарен оператор
    console.log((year % 4 === 0 && year % 100 != 0) || (year % 400 === 0) ? 'yes' : 'no');
}

//Invokation function
isYearLeap(1984);
isYearLeap(2024);
isYearLeap(300);