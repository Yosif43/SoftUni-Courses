pens = int(input())
markers = int(input())
liter_detergent = int(input())
discount = int(input())

price_pen = 5.80
price_marker = 7.20
price_detergent = 1.20

total_price_pen = pens * price_pen
total_price_markers = markers * price_marker
total_price_detergent = liter_detergent * price_detergent

total_sum = total_price_detergent + total_price_markers + total_price_pen
total_summ = total_sum - (total_sum * discount / 100)
print(total_summ)
