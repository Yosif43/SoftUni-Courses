//declare function
function printNumbers (m, n) {
    //диапазон от m до n
    //m = 6; n = 2 ->  [6; 2]
    //For -> имам определен брой пъти на изпълнение
    //повтаряме: отпечатваме числото
    //начало: m
    //край: n
    //промяна: -1
    for (let number = m; number >= n; number--) {
        console.log(number);
    }
}

//Invokation function
printNumbers(6, 2);
console.log('End');
printNumbers(4, 1);
console.log('End');
printNumbers(100, 10);
