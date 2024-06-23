### Machine Problem ###
# Print all the substrings  of length 2
# excluding the first and last characters


word = "programming"
 
for i in range(1,len(word)-2):
    print(word[i],word[i+1])
