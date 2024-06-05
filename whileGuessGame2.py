
secret_number = 5
user_input =0

while secret_number != user_input:
        user_input = int(input("Guess the number: "))
        if user_input > secret_number:
            print("The guess number is too high.")

        elif user_input < secret_number:
            print("The guess number is too low.")
            
        else:            
            print("You've guess the secret number.")     
                

        
        
                                    
        
        


        




