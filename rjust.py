def custom_rjust(s, width):
    if len(s) >= width:
        return s
    return ' ' * (width - len(s)) + s

text = input("Enter a string: ")
width = int(input("Enter the total width: "))

result = custom_rjust(text, width)
print("Result:", repr(result))
