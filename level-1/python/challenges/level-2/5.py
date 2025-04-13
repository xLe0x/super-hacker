# 5.​ Find prime numbers between 1 and 100.

for i in range(2, 101):
    is_prime = True
    for x in range(2, i):
        if i % x == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
