# Write your solution here

passwd = input("Password: ")

while True:
    rep_passwd = input("Repeat password: ")
    if passwd == rep_passwd:
        break
    print("They do not match!")
print("User account created!")
