function printCityInfo(city) {
    for (let key in city) {
        if (city.hasOwnProperty(key)) {
            console.log(`${key} -> ${city[key]}`);
        }
    }
}

// Example usage:
printCityInfo({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
});


printCityInfo({
    name: "Plovdiv",
    area: 389,
    population: 1162358,
    country: "Bulgaria",
    postCode: "4000"
});