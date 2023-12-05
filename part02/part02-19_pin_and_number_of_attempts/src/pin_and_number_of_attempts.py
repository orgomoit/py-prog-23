# Write your solution here

attempts = 0

while True:
    user_input = input("PIN: ")
    attempts += 1
    if user_input == "4321":
        break
    else:
        print("Wrong")

if attempts > 1:
    print(f"Correct! It took you {attempts} attempts")
else:
    print(f"Correct! It only took you one single attempt!")
