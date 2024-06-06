num_rows = 5


for i in range(1,num_rows+1): # print the number of rows

    for j in range(num_rows-i): # spaces
        print(" ", end="")

    for k in range(i): # print the asterisks
        print("*",end=" ")
    print()