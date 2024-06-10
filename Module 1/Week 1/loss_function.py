import sys
import math
import random

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

if __name__ == "__main__":
    calculate_loss_function()