def custom_islower(s):
    has_letter = False
    for char in s:
        if 'A' <= char <= 'Z':
            return False 
        if 'a' <= char <= 'z':
            has_letter = True  
    return has_letter  

text = input("Enter a string: ")

if custom_islower(text):
    print("All letters are lowercase.")
else:
    print("Not all letters are lowercase.")
