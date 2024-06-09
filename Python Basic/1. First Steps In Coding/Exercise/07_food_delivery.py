amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_vegetarian_menu = int(input())

delivery_price = 2.50
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

price_chicken_menu = amount_chicken_menu * chicken_menu
price_fich_menu = amount_fish_menu * fish_menu
price_vegetarian_menu = amount_vegetarian_menu * vegetarian_menu

total_sum = price_vegetarian_menu + price_fich_menu + price_chicken_menu
price_desert = total_sum * 20/100
total_sum = total_sum + price_desert + delivery_price
print(total_sum)