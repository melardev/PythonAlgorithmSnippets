sentence = "If you wait, all that happens is you get older ."
# split by spaces, get list of strings
words = sentence.split()
# reverse each item in the list and concatenate the items between them with space
reversed_sentence = " ".join(reversed(words))
print(reversed_sentence)
