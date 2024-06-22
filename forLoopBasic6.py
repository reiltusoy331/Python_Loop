print("### Determine the numbers in the list if its an EVEN or ODD. ###")
print()
digits =[2,3,4,5,6,8]
for num in range(len(digits)):
    number = digits[num]
    if number % 2==0:
        print(f"{number} is an EVEN number.")
    else:
        print(f"{number} is an ODD number.")

print() 



