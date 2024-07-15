import math
import random


def mae(n):
    sum_loss = 0
    for i in range(n):
        yt = random.uniform(0, 10)
        yp = random.uniform(0, 10)
        loss = abs(yt - yp)
        sum_loss += loss
        print(f'Sample {i}')
        print(f'pred: {yp}, target: {yt}, loss: {loss}')
    mae_value = sum_loss / n
    print(f'final MAE: {mae}')
    return mae_value


def mse(n):
    sum_loss = 0
    for i in range(n):
        yt = random.uniform(0, 10)
        yp = random.uniform(0, 10)
        loss = (yt - yp)**2
        sum_loss += loss
        print(f'Sample {i}')
        print(f'pred: {yp}, target: {yt}, loss: {loss}')
    mse_value = sum_loss / n
    print(f'final MSE: {mse}')
    return mse_value


def rmse(n):
    sum_loss = 0
    for i in range(n):
        yt = random.uniform(0, 10)
        yp = random.uniform(0, 10)
        loss = (yt - yp)**2
        sum_loss += loss
        print(f'Sample {i}')
        print(f'pred: {yp}, target: {yt}, loss: {loss}')
    mse = sum_loss / n
    rmse = math.sqrt(mse)
    print(f'final RMSE: {rmse}')
    return rmse


if __name__ == "__main__":
    num_samples = input('Enter number of sample: ')
    loss_name = input('Enter loss function (MAE, MSE, RMSE): ')

    if num_samples.isnumeric():
        num_samples = int(num_samples)
        if loss_name == 'MAE':
            mae(num_samples)
        if loss_name == 'MSE':
            mse(num_samples)
        if loss_name == 'RMSE':
            rmse(num_samples)
    else:
        print('number of samples must be an integer number')