from stock.turnover_rate import get
import pandas as pd
import time
import os
import shutil


data, time = get()
first_items = [item[0].split("  ")[0] for item in data[2:12]]
print(type(first_items))
data = pd.DataFrame(data)
folder_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA'
shutil.rmtree(folder_path, ignore_errors=True)
os.makedirs(folder_path, exist_ok=True)
for i in range(0, 3):
    file_name = f'{i}_cache.txt'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'a', encoding='UTF-8') as file:
        data.to_csv(file, header=False)
print(data)
