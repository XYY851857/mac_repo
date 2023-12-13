def data_dup(get_number, get_state, ori_lens):
    file_df = pd.read_csv('/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/股票抽籤DATA/DATA.txt', encoding='utf-8')
    number_data = file_df['number'][0:ori_lens + 1].tolist()
    state_data = file_df['state'][0:ori_lens + 1].tolist()
    new_lens = 0
    for slow_step in range(0, ori_lens):  # 慢指針
        if int(get_number[slow_step]) not in set(number_data):  # 判斷代號是否已在資料庫
            new_lens += 1
            continue
        else:  # 代號和資料庫重複
            for fast_step in range(len(state_data)):  # 快指針，定位number重複的位置並比對state是否相同
                if int(get_number[slow_step]) == int(number_data[fast_step]) and str(get_state[fast_step]) != str(
                        state_data[fast_step]):
                    new_lens += 1
                    continue
    # print(f'{get_number}\n{number_data}\n{new_lens}')
    return new_lens
