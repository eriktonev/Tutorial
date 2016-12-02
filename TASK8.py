word = str(input('Input word: '))#ask user for input

def removeVow(word):
    vow = ["a", "e", "i", "o", "u"]#the list of vowels
    chars = []#list of characters

    for i in word:
        if i.lower() not in vow:#check if the letters in the word are vowels
            chars.append(i)#adds everything but vowels to the chars list

    return "".join(chars)#makes it so it does not print out as a list

print(removeVow(word))#print out the answer
