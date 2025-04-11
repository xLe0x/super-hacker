# 9. Print "H4ck3r" with alternating uppercase and lowercase letters.
#          "h4cK3R"


def alter(string):
    res = ""
    for i in range(len(string)):
        if string[i].isalpha():
            if i % 2 == 0:
                res += string[i].lower()
            else:
                res += string[i].upper()
        else:
            res += string[i]
    return res


print(alter("H4ck3r"))
