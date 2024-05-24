
word="level"
is_palindrome = True

for i in range(len(word)//2):
    left_char = word[i]
    right_char = word[len(word)-i-1]

    #compare left_char and right_char
    if left_char.lower() != right_char.lower():
        is_palindrome = False

print(is_palindrome) 