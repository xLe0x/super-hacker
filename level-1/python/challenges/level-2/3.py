# 3.​ Create a script that prints every 4-digit PIN code (0000-9999).

for i in range(10000):

    print(str(i).zfill(4), end=" ")
