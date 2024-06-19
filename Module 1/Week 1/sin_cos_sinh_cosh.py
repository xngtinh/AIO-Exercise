import sys
import math
import random

# Calculate factorial value
mess = "N must be a positive integer"


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Calculate sin, cos, sinh, cosh


def calculate_sin(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError(mess)

    value = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        value += term
    print(value)


def calculate_cos(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError(mess)

    value = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        value += term
    print(value)


def calculate_sinh(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError(mess)

    value = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        value += term
    print(value)


def calculate_cosh(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError(mess)

    value = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        value += term
    print(value)


if __name__ == "__main__":
    calculate_sin(x=3.14, n=10)
    calculate_cos(x=3.14, n=10)
    calculate_sinh(x=3.14, n=10)
    calculate_cosh(x=3.14, n=10)
