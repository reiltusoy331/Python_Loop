num_rows =3
col = 1

for i in range(1,num_rows+1):
    for j in range(1,col+i):
        print("*",end='')
    col +=1
    print()