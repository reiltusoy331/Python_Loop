counter =1
print("Find a letter in a word")

text = input("Enter a word: ")
letter = input("What specific letter to find: ")


for char in text:
    print(f"Letter detected in iteration {counter} is: ",char)
    if char == letter:
        print(f"Found the {char} in iteration {counter}. ")
        print("Program will now terminate.")
        break
    counter+=1
