function updateInventory(stock, order) {
    let inventory = {};

    function addToInventory(items) {
        for (let i = 0; i < items.length; i += 2) {
            const product = items[i];
            const quantity = parseInt(items[i + 1]);
            if (inventory[product]) {
                inventory[product] += quantity;
            } else {
                inventory[product] = quantity;
            }
        }
    }

    addToInventory(stock);
    addToInventory(order);

    for (const product in inventory) {
        console.log(`${product} -> ${inventory[product]}`);
    }
}

updateInventory(
    ['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'], ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']
);

updateInventory(
    ['Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'], ['Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30']
);