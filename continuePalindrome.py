my_list=["madam","apple","noon","civil","civic","mum"]
my_palindrome = []

for word in my_list:
    if word == word[::-1]:
        my_palindrome.append(word)
    else:
        continue

print(my_palindrome)