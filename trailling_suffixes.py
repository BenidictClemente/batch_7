# Custom function to remove a suffix from the end of a string
def remove_suffix(s, suffix):
    if s.endswith(suffix):
        return s[:len(s) - len(suffix)]
    return s

text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

result = remove_suffix(text, suffix)
print("Result:", repr(result))
