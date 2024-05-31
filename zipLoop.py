# zip() funtion in for loops

a =[1,2,3,4]
b =[1,2,3,5]

for num1,num2 in zip(a,b):
    print("num1: ",num1," ", "num2: ",num2)


print()
print("Compare the two lists ")
print ("a =[1,2,3,4]")
print ("b =[1,2,3,5]")


are_equal = True
for num1,num2 in zip(a,b):
    if num1 != num2:
        are_equal = False

print(are_equal)