# Write your solution here

limit = int(input("Limit: "))

statement = "The consecutive sum: "

i = 1
sum = 0
while sum < limit:
    sum += i
    if sum >= limit:
        statement += f"{i}"
    else:
        statement += f"{i} + "
    i += 1

print(statement + " = " + str(sum))
