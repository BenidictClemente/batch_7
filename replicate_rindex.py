def custom_rindex(s, substring):
    for i in range(len(s)-len(substring), -1, -1):
        if s[i:i + len(substring)] == substring:
            return i 
    return -1  


text = input("Enter a string: ")
substring = input("Enter substring to find: ")


result = custom_rindex(text, substring)
if result != -1:
    print("The last occurrence is at index:", result)
else:
    print("Substring not found.")
