# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
sum = 0
pos = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    if num > 0:
        pos += 1
    count += 1
    sum += num

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / count}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {count - pos}")
