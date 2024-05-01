filename_plus_extension = input().split("\\")
filename, extension = filename_plus_extension[-1].split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")
