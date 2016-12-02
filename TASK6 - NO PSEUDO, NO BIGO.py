sentence = str(input('Input a sentence to be reversed: '))

words = sentence.split()
words_reversed = words[::-1]

print(' '.join(words_reversed))
