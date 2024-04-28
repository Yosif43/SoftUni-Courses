# string = input().split()
# result = ""
# for text in string:
#     lent = len(text)
#     result += text * lent
# print(result)
#
data = input().split()
new_text = [word * len(word) for word in data]
print("".join(new_text))
