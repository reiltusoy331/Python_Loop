
numbers = [1,2,3,4,5,6]

for i in range(len(numbers)):
    element = numbers[i]
    if element % 2 == 0:
        print(f'{element} is an even number.')
    else:
        print(f'{element} is an odd number.')
