word1="work"
word2=""
is_palindrome=True

for char in word1:
    print(char,end=' ')
    word2+=char
 
print()
print(word1)
print(word2)
if word1 != word2[::-1]:
    is_palindrome=False

print(is_palindrome)



