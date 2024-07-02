num_rows = 5

# num of iterations
for i in range(1,num_rows+1):

    # to print spaces
    for j in range(num_rows-i):
        print(" ",end='')
    
    # to print asterisk
    for k in range(i):
        print("*",end=' ')
    print()