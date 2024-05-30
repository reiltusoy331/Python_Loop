# Method 1

print("Method 1")
my_list = [1,5,7,9,6]

print(list(enumerate(my_list)))

print("")
print("Method 2")

for index, item in enumerate(my_list):
    print(index, item) 


print("")
print("Machine Problem")

for index, item in enumerate(my_list):
    if index % 2 != 0:
        item = item * 2
        print(index, item)
    else:
        print(index, item) 