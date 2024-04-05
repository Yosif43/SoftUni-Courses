input_list = input().split(" ")
palindrome = input()
palindrome_list = [i for i in input_list if i == i[::-1]]
print(palindrome_list)
print(f"Found palindrome {input_list.count(palindrome)} times")