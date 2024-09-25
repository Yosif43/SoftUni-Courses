def shop_from_grocery_list(budget, grocery_list, *products):
    bought_products = set()

    for product in products:
        product_name, product_price = product

        if product_name in grocery_list and product_name not in bought_products and budget >= product_price:
            bought_products.add(product_name)
            budget -= product_price

    missing_products = set(grocery_list) - bought_products
    if not missing_products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products_str = ', '.join(sorted(missing_products))
        return f"You did not buy all the products. Missing products: {missing_products_str}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))