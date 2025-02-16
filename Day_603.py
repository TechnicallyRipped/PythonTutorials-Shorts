



def is_palindrome(word:str) -> str:
    lowered_word = word.lower()
    if lowered_word == lowered_word[::-1]:
        return 'Palindrome!'
    else:
        return 'Not a palindrome'

print(is_palindrome('Racecar'))






