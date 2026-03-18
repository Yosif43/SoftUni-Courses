//Declare function
function calculateCircleArea (radius) {
    //площ / лице = pi * radius ^ 2
    let typeInputParameter = typeof radius; //'number' или е нещо друго (radius не е число => не мога да изчисля лицето)

    if (typeInputParameter === 'number') {
        //radius е число -> може да се изчисли лице -> 2 * radius * pi
        let area = Math.PI * radius ** 2
        console.log(area.toFixed(2));
    } else {
        //radius не е число -> не може да се изчисли лице
        console.log(`We can not calculate the circle area, because we received a ${typeInputParameter}.`);
    }
}

//Invokation function
calculateCircleArea(5);
calculateCircleArea('name');