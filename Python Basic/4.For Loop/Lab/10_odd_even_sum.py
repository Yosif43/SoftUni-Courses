n = int(input())
odd_summ = 0
even_sum = 0

for i in range(0, n):
    user_input = int(input())
    if i % 2 == 0:
        odd_summ += user_input
    else:
        even_sum += user_input

if odd_summ == even_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(odd_summ - even_sum)
    print("No")
    print(f"Diff = {diff}")
