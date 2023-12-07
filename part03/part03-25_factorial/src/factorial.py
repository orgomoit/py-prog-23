# Write your solution here

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    print(f"The factorial of the number {num} is {fact}")
print("Thanks and bye!")
