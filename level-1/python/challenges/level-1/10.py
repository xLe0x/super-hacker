# 10. Given password = "P@ssw0rd", replace all vowels with "*".


# password = "P@ssw0rd"
password = "xle0x"

vowels = "aieouAIEOU"
res = ""


for char in password:
    if char in vowels:
        res += "*"
    else:
        res += char


print(res)
