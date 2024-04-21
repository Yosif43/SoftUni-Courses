# def count_characters():
#     text = input()
#     char_counts = {}
#     for char in text:
#         if char != " ":
#             if char in char_counts:
#                 char_counts[char] += 1
#             else:
#                 char_counts[char] = 1
#
#     for char, count in char_counts.items():
#         print(f"{char} -> {count}")
#
# count_characters()

symbols = [char for char in input() if char != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for character, occurrences in letters.items():
    print(f"{character} -> {occurrences}")
