function calculateOrderTotal(product, quantity) {
    let pricePerUnit;

    switch (product) {
        case "coffee":
            pricePerUnit = 1.50;
            break;
        case "water":
            pricePerUnit = 1.00;
            break;
        case "coke":
            pricePerUnit = 1.40;
            break;
        case "snacks":
            pricePerUnit = 2.00;
            break;
        default:
            console.log("Invalid product");
            return;
    }

    let total = pricePerUnit * quantity;
    console.log(total.toFixed(2));
}

// Example usage:
calculateOrderTotal("water", 5); // Outputs: 5.00
calculateOrderTotal("coffee", 2); // Outputs: 3.00