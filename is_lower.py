def custom_islower(s):
    has_letter = False
    for char in s:
        if 'A' <= char <= 'Z':
            return False  # Found an uppercase letter
        if 'a' <= char <= 'z':
            has_letter = True  # At least one lowercase letter exists
    return has_letter  # Return True only if there's at least one lowercase letter

# --- User Input ---
text = input("Enter a string: ")

# --- Result ---
if custom_islower(text):
    print("All letters are lowercase.")
else:
    print("Not all letters are lowercase.")
