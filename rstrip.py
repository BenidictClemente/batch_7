# Custom function to remove spaces from the end
def remove_trailing_spaces(s):
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    return s[:i+1]

# --- User Input ---
text = input("Enter a string: ")

# --- Result ---
result = remove_trailing_spaces(text)
print("Result:", repr(result))
