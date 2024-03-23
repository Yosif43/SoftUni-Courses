circle = list(map(int, input().split()))
k = int(input())

def josephus_permutation(circle, k):
    result = []
    index = 0

    while len(circle) > 0:
        index = (index + k - 1) % len(circle)
        executed = circle.pop(index)
        result.append(executed)

    return result
permutation = josephus_permutation(circle, k)
print(f"[{','.join(map(str, permutation))}]")
