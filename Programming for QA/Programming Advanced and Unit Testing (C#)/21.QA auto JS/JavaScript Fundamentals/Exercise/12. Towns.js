function getTownsTable(arrayData) {
    const townData = [];
    for (let dataText of arrayData) {
        const splittedData = dataText.split(' | ');
        let town = splittedData[0]
        let latitude = splittedData[1]
        let longitude = splittedData[2]

        townData.push({
            town: town,
            latitude: parseFloat(latitude).toFixed(2),
            longitude: parseFloat(longitude).toFixed(2),
        })
    }

    townData.forEach((town) => console.log(town));
}

getTownsTable(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625'
])
getTownsTable(['Plovdiv | 136.45 | 812.575'])