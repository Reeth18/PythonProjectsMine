string1 = input("Enter a string: ")
uniqueLetters = []

for char in string1:
    if char.isalpha() and char.lower() not in uniqueLetters:
        uniqueLetters.append(char.lower())
        
print("Unique letters:", ", ".join(uniqueLetters))
print("Number of unique letters:", len(uniqueLetters))
