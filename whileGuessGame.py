
secret_number = 5
i=0
max_trial =5


while i != max_trial:
        user_input = int(input("Guess the number: "))
        if user_input > secret_number:
            print("The guess number is too high.")

        elif user_input < secret_number:
            print("The guess number is too low.")
            
        elif user_input == secret_number:      
            print("You've guess the secret number.")
                                    
        else:
            print(f"You've reached the max trial. The secret number is {secret_number}")                  
        max_trial -= 1                  


        




