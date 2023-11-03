"""
給一個連結陣列，交換兩兩相鄰的節點並且回傳。
範例： 1->2->3->4, return 2->1->4->3。
你的演算法不能改變節點裡面的值，只能把節點搬來搬去。
"""


def algo(list):
    list[0], list[1] = list[1], list[0]
    list[2], list[3] = list[3], list[2]
    return list


if __name__ == "__main__":
    list = ['1', '2', '3', '4']
    list_r = algo(list)
    ans = '->'.join(map(str, list_r))
    print(ans)
