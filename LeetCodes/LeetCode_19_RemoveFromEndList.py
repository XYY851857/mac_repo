"""
給一個連結陣列，移除連結陣列從後面數來第n個節點
例如，
   1->2->3->4->5, n = 2.
   從後面數2個，移除4後的連結陣列變成 1->2->3->5.
注意:
n不會比連結陣列還長，試著跑一次迴圈解題。
"""


def algo1(data):
    link_str = '->'.join(map(str, data))
    return link_str




def algo2(data):
    link_str = ''
    for num in data:
        link_str += str(num) + '->'
    link_str = link_str[:-2]
    return link_str


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    n = 2
    ans1 = algo1(list)
    ans2 = algo2(list)
    print(ans1)
    print(ans2)

