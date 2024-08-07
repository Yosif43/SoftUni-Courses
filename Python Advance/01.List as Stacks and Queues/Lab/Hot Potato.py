from collections import deque

name = deque(input().split())
n = int(input()) - 1

while len(name) != 1:
    name.rotate(-n)
    print(f"Removed {name.popleft()}")

print(f"Last is {name.popleft()}")

