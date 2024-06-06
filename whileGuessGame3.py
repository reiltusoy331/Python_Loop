
secret_number = 5
i=0
max_trial =5


while i != max_trial:
        user_input = int(input("Guess the number: "))
        if user_input > secret_number:
            print("The guess number is too high.")

        elif user_input < secret_number:
            print("The guess number is too low.")
            
        else:
            print("You've guess the secret number.")                                    
            break
        max_trial -= 1                  
        if max_trial==0:
            print(f"\nYou've reached the max trial. The secret number is {secret_number}")                  


        




