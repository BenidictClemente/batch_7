def custom_startswith(s, prefix):
    
    return s[:len(prefix)] == prefix
prefix = "pre, re"
text = input("Enter a string: ")


if custom_startswith(text, prefix):
    print("The string starts with the given prefix.")
else:
    print("The string does not start with the given prefix.")
