### Machine Problem: Reversing Casing ###

my_string = "Learning Loops"
new_string = ""

for char in my_string:
    if char.isupper():
        new_string += char.lower()
    else:
        new_string += char.upper()

print(new_string)


print()


letters = "aaabbbcccdddfffggg"
new_letter =""

for letter in letters:
    if letter not in new_letter:
        new_letter += letter

print(new_letter)








