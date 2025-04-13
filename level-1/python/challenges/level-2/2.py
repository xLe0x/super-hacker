# 2.​ Print all numbers from 1 to 100 except numbers divisible by 4.

for i in range(1, 100 + 1):
    if i % 4 != 0:
        print(i, end=" ")
