def data_dup(var1, var2, var_lens):
    file_df = pd.read_csv('data locate', encoding='utf-8')
    data1 = file_df['header'][0:var_lens + 1].tolist()
    data2 = file_df['header'][0:var_lens + 1].tolist()
    new_lens = 0
    for slow_step in range(0, var_lens):  # 慢指針
        if int(var1[slow_step]) not in set(data1):  # 判斷代號是否已在資料庫
            new_lens += 1
            continue
        else:  # 代號和資料庫重複
            for fast_step in range(len(data2)):  # 快指針，定位number重複的位置並比對state是否相同
                if int(var1[slow_step]) == int(data1[fast_step]) and str(var2[fast_step]) != str(
                        data2[fast_step]):
                    new_lens += 1
                    continue
    # print(f'{var1}\n{data1}\n{new_lens}')
    return new_lens
