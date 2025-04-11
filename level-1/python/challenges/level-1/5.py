# 5. Reverse the string “rekcah_repus” without using built-in functions.


def reverse_string():
    string = "rekcah_repus"
    res = ""
    for i in range(len(string), 0, -1):
        res += string[i - 1]

    return res


print(reverse_string())
