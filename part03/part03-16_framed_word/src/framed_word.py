# Write your solution here

word = input("Word: ")

print("*" * 30)
if len(word) % 2 == 0:
    spaces = " " * ((30 - len(word) - 2) // 2)
    print("*" + spaces + word + spaces + "*")
else:
    spaces = " " * ((30 - len(word) - 2) // 2)
    print("*" + spaces + word + spaces + " " + "*")
print("*" * 30)
