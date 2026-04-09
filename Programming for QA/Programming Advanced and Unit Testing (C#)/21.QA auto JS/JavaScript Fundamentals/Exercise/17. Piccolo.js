function parkLot(input) {

    let cars = new Map();

    for (const command of input) {
        let currCommandArray = command.split(', ');
        let currentCommand = currCommandArray[0];
        let currentCarNumber = currCommandArray[1];
        if (currentCommand === 'IN') {
            cars.set(currentCarNumber, true);
        } else if (currentCommand === 'OUT') {
            cars.set(currentCarNumber, false);
        }
    }

    const sortedCars = new Map(
        [...cars.entries()].sort()
    );

    let isEmpty = true;

    for (const car of sortedCars) {

        if (car[1]) {
            console.log(car[0]);
            isEmpty = false;
        }
    }

    if (isEmpty) {
        console.log('Parking Lot is Empty');
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