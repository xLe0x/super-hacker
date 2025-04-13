# 10.​Check if a string is a palindrome (same forward and backward).

string = input("Enter any string: ")
reversed_string = "".join([string[i] for i in range(len(string) - 1, -1, -1)])

if string == reversed_string:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
