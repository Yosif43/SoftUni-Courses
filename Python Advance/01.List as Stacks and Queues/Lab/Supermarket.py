from collections import deque

name = input()
paid_list = deque()


while name != "End":
    if name == "Paid":
        while paid_list:
            print(paid_list.popleft())
    else:
        paid_list.append(name)
    name = input()
print(f"{len(paid_list)} people remaining.")
