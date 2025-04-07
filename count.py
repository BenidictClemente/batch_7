def custom_count(s, substring):
    count = 0
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            count += 1
    return count

text = input("Enter a string: ")
substring = input("Enter substring to count: ")

result = custom_count(text, substring)
print("The substring appears", result, "times.")
