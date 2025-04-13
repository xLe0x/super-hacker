# 1.​ Write a script that asks for a password and only allows access if it matches "s3cr3t".

password = input("What is the secret password? ")

if password == "s3cr3t":
    print("Welcome Hacker!")
else:
    print("Not a correct password")
