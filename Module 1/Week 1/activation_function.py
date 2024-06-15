import sys
import math
import random

# Check value
def is_number(n):
    try :
        float ( n ) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

# Calculate activation function
def calculate_activation_function():
    value = 0
    x = input("Input x = ")

    if not is_number(x):
        print("x must be a number")
        sys.exit()

    x = float(x)
    activation_function = input("Input activation function ( sigmoid | relu | elu ) : ")

    if activation_function == "sigmoid":
        value = 1 / (1 + math.exp(-x))
    elif activation_function == "relu":
        if x > 0:
            value = x
        else:
            value = 0
    elif activation_function == "elu":
        if x > 0:
            value = x
        else:
            value = 0.01 * (math.exp(x) - 1)
    else:
        print(f"{activation_function} is not supported")
        sys.exit()
    
    print(f"{activation_function}: f({x}) = {value}")

if __name__ == "__main__":
    calculate_activation_function()