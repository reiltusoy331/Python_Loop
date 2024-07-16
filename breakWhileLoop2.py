
data =[]

print("Enter any number, to stop enter \"-1\".")
print()
while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    data.append(number)

print()
print("The entered numbers in list format: ",data)
