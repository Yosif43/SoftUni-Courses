head = input()
body = input()
tail = input()

animal_list = [tail, body, head]

print(animal_list)

tail = input()
body = input()
head = input()
meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)