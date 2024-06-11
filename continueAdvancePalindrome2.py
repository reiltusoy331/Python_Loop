def is_palindrome(word):
    return word ==word[::-1]

my_list=["madam","apple","noon","civil","civic"]
my_palindrome = []

for word in my_list:
    if not is_palindrome(word.lower()):
        continue
    my_palindrome.append(word)

print(my_palindrome)




    
