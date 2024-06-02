list_numbers = [11,12,3,41,15,26]
grades = {"Anna":97, "Jane":90,"AJ":95}

print("Reverse() in for loop")
for number in reversed(list_numbers):
    print(number)

print()
print(list(reversed(list_numbers)))


print()
print(list(reversed(grades.keys())))