# Write your solution here

sentence = ""
prev_word = ""

while True:
    curr_word = input("Please type in a word: ")
    if curr_word == "end" or curr_word == prev_word:
        break
    sentence += curr_word + " "
    prev_word = curr_word

print(sentence)