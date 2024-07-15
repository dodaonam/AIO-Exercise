import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return 0 if x <= 0 else x


def elu(x):
    alpha = 0.01
    return alpha * (math.exp(x) - 1) if x <= 0 else x


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    x = input('Enter x: ')
    name_function = input('Enter name activation function: ')

    if is_number(x):
        x = float(x)
        if name_function == 'sigmoid':
            print(f"sigmoid: f({x}) = {sigmoid(x)}")
        elif name_function == 'relu':
            print(f"relu: f({x}) = {relu(x)}")
        elif name_function == 'elu':
            print(f"elu: f({x}) = {elu(x)}")
        else:
            print('The provided activation function is not supported')
    else:
        print('x must be a number')