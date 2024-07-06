num_row =5

#iterations of the loop
for row in range(num_row,0,-1):

    #print the spaces
    for space in range(0,num_row-row):
        print(end=' ')

    #print the asterisks
    for asterisk in range(row):
        print("*",end=' ')
    print()