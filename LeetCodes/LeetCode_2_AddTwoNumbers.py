"""
給您兩個表示兩個非負整數的非空鍊錶。這些數字以相反的順序存儲，並且它們的每個節點都包含一個數字。將兩個數字相加並以鍊錶形式傳回總和。
您可以假設這兩個數字不包含任何前導零，除了數字 0 本身。
輸入： l1 = [2,4,3], l2 = [5,6,4]
輸出： [7,0,8]
解釋： 342 + 465 = 807。
限制條件：
每個鍊錶中的節點數在範圍 內[1, 100]。
0 <= Node.val <= 9
保證清單代表一個沒有前導零的數字。
"""


def algo(list1, list2):
    list_algo = []
    for i in range(len(list1)):
        list_algo.extend([list1[i] + list2[i]])
    return list_algo


def decimal(data):
    for i in range(len(data)):
        if data[i] >= 10 and i == 0:
            data[i] %= 10
            data.insert(0, 1)
        elif data[i] >= 10:
            data[i] = data[i] % 10
            data[i - 1] += 1
    return data


if __name__ == "__main__":
    list1, list2 = [2, 4, 3], [5, 6, 4]
    my_list = algo(list1, list2)
    ans = decimal(my_list)
    print(ans)
