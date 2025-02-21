import itertools


def possible_permutations(ls: list):
    for perm in itertools.permutations(ls):
        yield list(perm)


# def possible_permutations(ls: list):
#     if len(ls) <= 1:
#         yield ls
#     else:
#         for i in range(len(ls)):
#             for perm in possible_permutations(ls[:i] + ls[i + 1:]):
#                 yield [ls[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]
