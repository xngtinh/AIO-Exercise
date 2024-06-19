import sys
import math
import random

# Calculate Mean difference of n_th root error


def md_nre_single_sample(y, y_hat, n, p):
    value = (y ** (1/n) - y_hat ** (1/n)) ** p
    print(value)


if __name__ == "__main__":
    md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)
