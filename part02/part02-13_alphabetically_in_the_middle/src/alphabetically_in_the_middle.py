# Write your solution here

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second and first > third:
    if second > third:
        middle = second
    else:
        middle = third
elif second > third:
    if third > first:
        middle = third
    else:
        middle = first
else:
    if second > first:
        middle = second
    else:
        middle = first
# elif second > third and second > first:
#     if third > first:
#         middle = third
#     else:
#         middle = first
# elif third > first and third > second:
#     if first > second:
#         middle = first
#     else:
#         middle = second

print(f"The letter in the middle is {middle}")
