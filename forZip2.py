a = [1,2,3,4]
b = [1,2,3,4,5,6]


for num1,num2 in zip(a,b):
    print(f"num 1 - {num1} and num 2 - {num2}")

print()

print(list(zip(a,b)))

