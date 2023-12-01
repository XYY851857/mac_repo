import pandas as pd
import os

stock_id = '2329'
folder_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA'
file_name = f'{stock_id}_cache.txt'
file_path = os.path.join(folder_path, file_name)

with open(file_path, 'r', encoding='UTF-8') as file:
    print(file)
    data = file.read().strip().replace('\n',',').split(',')
    print(data)
    formatted_data = [data[i:i + 7] for i in range(0, len(data), 7)]
    list_pd = pd.DataFrame(formatted_data)

print(list_pd)
