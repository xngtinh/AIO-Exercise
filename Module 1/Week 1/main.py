import sys
import math
import random

# Print variable
def print_function():
    var1 = 'str_var1'
    var2 = 3
    var3 = 15.5

    print('Print single variablee (var1): ', var1)
    print(f'Print more than one variable: var1={var1}, var2={var2}, var3={var3}')

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

# Calculate loss function
def calculate_loss_function():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isdigit():
        print("Number of samples must be an integer number.")
        sys.exit()

    loss_name = input("Input loss name (MAE, MSE, or RMSE): ")

    num_samples = int(num_samples)
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        
        if loss_name == "MAE":
            loss = abs(predict - target)
        elif loss_name == "MSE":
            loss = (predict - target) ** 2
        else:
            loss = math.sqrt((predict - target) ** 2)
        
        print(f"Loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")

# Calculate factorial value
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Calculate sin, cos, sinh, cosh
def calculate_sin(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n must be a positive integer")

    value = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        value += term
    print(value)

def calculate_cos(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n must be a positive integer")

    value = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        value += term
    print(value)

def calculate_sinh(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n must be a positive integer")

    value = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        value += term
    print(value)

def calculate_cosh(x, n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n must be a positive integer")

    value = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        value += term
    print(value)

# Calculate Mean difference of n_th root error
def md_nre_single_sample(y, y_hat, n, p):
    value = (y ** (1/n) - y_hat ** (1/n)) ** p
    print(value)

if __name__ == "__main__":
    # print_function()
    # print("**********")

    # f1_score(tp="a", fp=3, fn=4)
    # print("**********")

    # calculate_activation_function()
    # print("**********")

    # calculate_loss_function()
    # print("**********")

    # calculate_sin(x=3.14, n=10)
    # calculate_cos(x=3.14, n=10)
    # calculate_sinh(x=3.14, n=10)
    # calculate_cosh(x=3.14, n=10)
    # print("**********")

    md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)