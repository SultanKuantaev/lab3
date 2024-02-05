word = input("write a word: ")

def polindrome(word):
    word2 = word[::-1]
    if(word == word2):
        return "Yes"
    else:
        return "NO"
print(polindrome(word))    