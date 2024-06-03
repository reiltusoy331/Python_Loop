continue_loop = True

while continue_loop:
    print("Please enter two integers: ")
    num1=int(input())
    num2=int(input())

    print(f'{num1} + {num2} = {num1+num2}')

    print("Would you like to enter two new integers again?")
    answer = input("Please enter 'yes' or 'no': ")

    if answer =='no':
        continue_loop=False

print("Loop ends here.")