month = input()
nights_qtu = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = nights_qtu * 50.00
    apartment_price = nights_qtu * 65.00
    if nights_qtu > 7 and nights_qtu <= 14:
        studio_price -= studio_price * 0.05
    elif nights_qtu > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10

elif month == "June" or month == "September":
    studio_price = nights_qtu * 75.20
    apartment_price = nights_qtu * 68.70
    if nights_qtu > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10

elif month == "July" or month == "August":
    studio_price = nights_qtu * 76.00
    apartment_price = nights_qtu * 77.00
    if nights_qtu > 14:
        apartment_price -= apartment_price * 0.10

print(f'Apartment: {apartment_price :.2f} lv.')
print(f'Studio: {studio_price :.2f} lv.')
