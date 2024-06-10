import sys
import math
import random

# Calculate F1-score
def f1_score(tp, fp, fn):
    if type(tp) is not int:
        print("tp must be int")
        sys.exit()
    elif type(fp) is not int:
        print("fp must be int")
        sys.exit()
    elif type(fn) is not int:
        print("fn must be int")
        sys.exit()

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        sys.exit()

    precision = tp / (tp + fp)
    recall = tp / (tp+fn)
    f1 = 2 * (precision * recall) / (precision + recall)

    print("Precision is ", precision)
    print("Recall is ", recall)
    print("f1-score is ", f1)

if __name__ == "__main__":
    f1_score(tp="a", fp=3, fn=4)