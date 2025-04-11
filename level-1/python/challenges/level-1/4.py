# 4. Create a program that asks for two numbers and prints their sum, difference, product, and quotient.


def sum(a, b):
    return a + b


def difference(a, b):
    return a - b


def product(a, b):
    return a * b


def quotient(a, b):
    return a / b


def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    print(f"Sum: {sum(num1, num2)}")
    print(f"difference: {difference(num1, num2)}")
    print(f"product: {product(num1, num2)}")
    print(f"quotient: {quotient(num1, num2)}")


main()
