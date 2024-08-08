from collections import deque

quantity_food = int(input())
queue_orders = deque([int(x) for x in input().split()])

print(max(queue_orders))

while queue_orders and queue_orders[0] <= quantity_food:
    quantity_food -= queue_orders[0]
    queue_orders.popleft()

if queue_orders:
    print("Orders left:", end="")
    while queue_orders:
        print(f" {queue_orders.popleft()}", end="")
else:
    print("Orders complete")
