a = [1,2,3,4]
b = [1,2,3,4]
equal_values = True

for i in zip(a,b):
    if a != b:
        equal_values = False

print(equal_values)
