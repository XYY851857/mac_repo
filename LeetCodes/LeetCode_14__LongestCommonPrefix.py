"""
一個陣列中有許多個字串，寫一個function找出這些字串最長的共同字首。
範例：
['abcd','abccc','abdec'] --> 共同字首為 'ab' 。
"""


def find(data):
    if not data:
        return ''

    min_len = min(len(word)for word in data)
    list_r1, list_r2, list_r3, list_ans = [], [], [], []
    for item in range(len(data)):
        list_r1.extend(data[0])
        list_r2.extend(data[1])
        list_r3.extend(data[2])
    min_len = min(len(word) for word in data)
    for turn in range(min_len):
        if list_r1[turn] == list_r2[turn] == list_r3[turn]:
            list_ans.append(list_r1[turn])
    return list_ans


if __name__ == '__main__':
    list1 = ['abcd', 'abccdc', 'abcec']
    ans = find(list1)
    print(ans)
