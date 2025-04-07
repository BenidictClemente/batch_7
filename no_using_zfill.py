def custom_zfill(s, width):
    if len(s) >= width:
        return s
    return '0' * (width - len(s)) + s

text = input("Enter a string: ")
width = int(input("Enter the total width: "))

result = custom_zfill(text, width)
print("Result:", repr(result))
