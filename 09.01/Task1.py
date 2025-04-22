def is_palindrom(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True


print(is_palindrom(str("шалар")))
