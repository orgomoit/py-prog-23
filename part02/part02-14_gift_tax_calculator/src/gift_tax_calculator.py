# Write your solution here

gift_value = int(input("Value of gift: "))

if gift_value < 5000:
    amount = 0
elif gift_value < 25000:
    amount = (100 + (gift_value - 5000) * 0.08)
elif gift_value < 55000:
    amount = (1700 + (gift_value - 25000) * 0.10)
elif gift_value < 200000:
    amount = (4700 + (gift_value - 55000) * 0.12)
elif gift_value <= 1000000:
    amount = (22100 + (gift_value - 200000) * 0.15)
else:
    amount = (142100 + (gift_value - 1000000) * 0.17)

if amount == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {amount} euros")
