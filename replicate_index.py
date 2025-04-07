def custom_index(s, substring):
    for i in range(len(s)):
        if s[i:i + len(substring)] == substring:
            return i 
    return -1  


text = input("Enter a string: ")
substring = input("Enter substring to find: ")

result = custom_index(text, substring)
if result != -1:
    print("The first occurrence is at index:", result)
else:
    print("Substring not found.")
