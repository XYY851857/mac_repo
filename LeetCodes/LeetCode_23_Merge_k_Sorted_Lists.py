"""
給你一個k個鍊錶數組lists，每個鍊錶都按升序排序。
將所有鍊錶合併為一個已排序的鍊錶並傳回。
範例1：
輸入： 列表 = [[1,4,5],[1,3,4],[2,6]]
輸出： [1,1,2,3,4,4,5,6]
說明：連結列表為：
[
  1->4->5,
  1->3->4,
  2->6
]
將它們合併到一個排序列表中：
1->1->2->3->4->4->5->6
範例2：
輸入： 列表 = []
輸出： []
範例3：
輸入： 列表 = [[]]
輸出： []
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def create_link_list(list1):
    # print(list1)
    if not list1 or len(list1) == 0:
        return None
    head = ListNode(list1[0])
    current = head
    for num in list1[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def merge(list1, list2):
    dummy = ListNode(0)
    current = dummy


    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


def merge_sort(list):
    if not list:
        return None
    merge_head = list[0]
    for i in range(1, len(list)):
        merge_head = merge(merge_head, list[i])

    return merge_head


if __name__ == "__main__":
    list1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [create_link_list(sublist) for sublist in list1]
    merge_head = merge_sort(linked_lists)
    current = merge_head
    while current:
        print(current.value, end='->')
        current = current.next

