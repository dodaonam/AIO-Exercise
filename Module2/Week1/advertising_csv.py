import numpy as np
import pandas as pd

df = pd . read_csv ('D:\\AIO Exercise\\AIO-Exercise\\advertising.csv')
data = df . to_numpy ()
print(data[:5])

sales_data = data[:, 3]
sales_max = np.max(sales_data)
sales_max_index = np.argmax(sales_data)
print(f'Max: {sales_max} - Index: {sales_max_index}')

tv_data = data[:, 0]
tv_mean = np.mean(tv_data)
print(tv_mean)

count = np.sum(sales_data >= 20)
print(count)

radio_data = data[:, 1]
sale_cond = sales_data >= 15
print(np.mean(radio_data[sale_cond]))

news_data = data[:, 2]
news_cond = news_data > np.mean(news_data)
print(np.sum(sales_data[news_cond]))

A = np.mean(sales_data)
scores = np.where(sales_data < A, 'Bad', np.where(sales_data > A, 'Good', 'Average'))
print(scores[7:10])

sub_abs = abs(sales_data - A)
avg_idx = np.argmin(sub_abs)
A = sales_data[avg_idx]
scores = np.where(sales_data < A, 'Bad', np.where(sales_data > A, 'Good', 'Average'))
print(scores[7:10])