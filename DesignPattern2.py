num_row = 3

for i in range(num_row,0,-1):
    print(" "*(i-1)+"* "*((num_row+1)-i))
for j in range(num_row):
    print(" "*(j+1)+"* "*(num_row-1-j))

#  Target Pattern Printing
#
#          * 
#         * * 
#        * * *
#         * * 
#          * 
