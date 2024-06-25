fruits =['apple','banana','calamansi']

for index, item in enumerate(fruits,1):
    print(f"The fruit at index {index} is {item}.")

print() 
print()
veggies =['asparagus','brocolli','carrots','squash']

for indx, itm in enumerate(veggies):
    if indx %2 != 0:
        veggies[indx] = itm*2
        print(f"The fruit at index {indx} is {itm}.")