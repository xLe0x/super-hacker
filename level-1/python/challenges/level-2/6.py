# 6.​ Simulate a login attempt system that locks after 3 failed attempts.

tries = 0

while tries < 3:
    password = input("Enter the password: ")
    if password != "s3cr3t":
        tries += 1
        print("Incorrect password")


print("Your have been blocked!")
