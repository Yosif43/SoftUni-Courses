def nums_sums(*args):
    neg_sum = 0
    pos_sum = 0
    for num in args:
        if num > 0:
            pos_sum += num
        else:
            neg_sum += num
    return neg_sum, pos_sum



numbers = [int(x) for x in input().split()]

print(nums_sums(*numbers)[0])
print(nums_sums(*numbers)[1])
if abs(nums_sums(*numbers)[0]) > nums_sums(*numbers)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
