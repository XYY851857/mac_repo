"""
這是一個算完說出來的序列，序列如下：
1, 11, 21, 1211, 111221, ...

1     讀做 1個1， 所以下一個變成 11
11    讀做 2個1， 也就是21
21    讀做 1個2 1個1，得到1211
1211  1個1，1個2，2個1  111221
"""


def algo(seq):
    next_seq = []
    i = 0
    while i < len(seq):
        count = 1
        while i < len(seq) - 1 and seq[i] == seq[i + 1]:
            count += 1
            i += 1
        next_seq.extend([str(count), seq[i]])
        i += 1
    return ''.join(next_seq)


if __name__ == "__main__":
    seq = "1"
    times = int(input("生成行數： "))
    for _ in range(times):
        print(seq)
        seq = algo(seq)
