# Fix the program

points = int(input("How many points are on your card? "))

# card_points = points

if points < 100:
    # card_points *= 1.1
    factor = 1.1
    print("Your bonus is 10 %")
if points >= 100:
    # card_points *= 1.15
    factor = 1.15
    print("Your bonus is 15 %")
points = points * factor

print("You now have", points, "points")