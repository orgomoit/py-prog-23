# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

i = word.find(char)
if (i != -1) and (i + 3) <= len(word):
    print(word[i:i+3])
# if i + 3 < len(word):
#     print(word[i:i+3])
