function parkLot(commands) {
    // Решение с масив - работи по условието, но не се харесва на Judge
    let cars = [];

    for (let i = 0; i < commands.length; i++) {
        let currentCommand = commands[i].split(', ');
        if (currentCommand[0] === 'IN') {
            cars.push(currentCommand[1].trim());
        } else if (currentCommand[0] === 'OUT') {
            cars.splice(cars.indexOf(currentCommand[1]), 1);
        }
    }

    if (cars.length === 0) {
        console.log('Parking Lot is Empty');
    } else {
        cars.sort((a, b) => a.localeCompare(b));
        for (const car of cars) {
            console.log(car);
        }
    }
}

parkLot(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU'
]);

parkLot(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA'
]);