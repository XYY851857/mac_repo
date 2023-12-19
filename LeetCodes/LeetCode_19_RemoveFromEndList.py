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


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove(head, n):
    dummy = ListNode(0)  # 節點初始化，避免野指針
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):  # 定位要移除的位置
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next  # 將slow的下一個節點定義為再下一個，也就是將fast.next移除

    return dummy.next



if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    n = 0

    head = ListNode(list1[0])  # 定義標頭
    current = head  # 給迴圈用標頭
    for num in list1[1:]:  # 用迭代方式定義整個列表，由於第一項已經定義為標頭不需迭代，故迴圈起始點設為1
        current.next = ListNode(num)  # 設定當前節點的下一個節點
        current = current.next  # 將下一個節點設為當前節點

    new_head = remove(head, n)

    result = []
    while new_head is not None:
        result.append(new_head.value)
        new_head = new_head.next

    ans = algo1(result)


    print(ans)

