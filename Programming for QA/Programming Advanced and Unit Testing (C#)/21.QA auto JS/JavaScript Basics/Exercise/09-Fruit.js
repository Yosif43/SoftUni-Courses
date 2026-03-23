//Declare Function
function fruit(fruit, grams, price_per_kg) {
    let price = (grams / 1000) * price_per_kg
    console.log(`I need $${price.toFixed(2)} to buy ${(grams / 1000).toFixed(2)} kilograms ${fruit}.`);
}