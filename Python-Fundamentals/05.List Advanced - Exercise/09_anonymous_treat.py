data = input().split()
result = []

while True:
    command = input()
    if command == "3:1":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "merge":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        merged = ''.join(data[start_index:end_index + 1])
        data = data[:start_index] + [merged] + data[end_index + 1:]
    elif action == "divide":
        index = int(command_parts[1])
        partitions = int(command_parts[2])
        element = data[index]
        partition_length = len(element) // partitions
        divided = [element[i:i + partition_length] for i in range(0, len(element), partition_length)]
        data = data[:index] + divided + data[index + 1:]

result = (' '.join(data))
print(result)
