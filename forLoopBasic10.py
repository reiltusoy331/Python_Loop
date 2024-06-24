### Machine Problem ###
# Store the odd numbers from 1 to 50 to an array

odd_numbers =[]

for i in range(1,50):
    if i %2 != 0:
        odd_numbers.append(i)

print(odd_numbers)
  