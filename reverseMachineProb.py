#### Machine Problem ####
# Problem 1: Reverse Casing
# Hello --> hELLO


word = "PROGramming"
new_word =""

print("Problem 1: Reverse Casing")
for char in word:
    if char in char.upper():
        new_word += char.lower()
    else: 
        new_word += char.upper()

print(new_word)

print("\n")


print("Problem 2: Remove Duplicate Letter")

my_word = "tomorrow"
my_new_word =""


for letter in my_word:
    if letter.lower() not in my_new_word:
        my_new_word += letter.lower()

print(my_new_word)

