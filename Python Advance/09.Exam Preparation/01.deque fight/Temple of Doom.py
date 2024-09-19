from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = deque(map(int, input().split()))

while challenges:
    result = tools[0] * substances[-1]

    if result in challenges:
        challenges.remove(result)
        tools.popleft()
        substances.pop()

    else:
        tools.append(tools.popleft() + 1)

        if substances[-1] == 1:
            substances.pop()
        else:
            substances[-1] -= 1

    if not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")


print("Tools:", end=" ")
print(*tools)
print("Substances:", end=" ")
print(*substances)
print("Challenges:", end=" ")
print(*challenges)

