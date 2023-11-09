"""
使用stacks來實做queue。

push(x) -- 將一個元素x放入queue最後
pop() -- 移除queue最前面的元素
peek() -- 取得queue最前面的元素(不刪除)
empty() -- 檢查queue是否是空的
注意：
你只能用標準的stack方法操作，這表示只有push到stack頂端， peek/pop stack頂端的元素， size， isEmpty這些方法是可以用的。

有些語言可能沒有支援stack，你可以使用類似的結構，例如list或deque, 只要你的操作符合上述的標準stack方法。可以假設全部的操作都是合法的(例如說當queue是empty的時候，不會執行pop這樣的操作)。
"""

import queue

if __name__ == "__main__":
    """push(x) -- 將一個元素x放入queue最後"""
    print('Part 1')
    my_queue = queue.Queue()
    x = 6
    my_queue.put(x)
    ans1 = my_queue.get_nowait()
    print(f'ans1 = {ans1}')
    """pop() -- 移除queue最前面的元素"""
    print('\nPart 2')
    my_queue.put('hello')
    my_queue.put('world')
    try:
        ans2 = my_queue.get_nowait()
        print(ans2)
        ans2 = my_queue.get_nowait()
        print(ans2)
        ans2 = my_queue.get_nowait()
    except queue.Empty:
        print('! Queue Empty !')
    """peek() -- 取得queue最前面的元素(不刪除)"""
    print('\nPart3')
    my_queue.put('hello')
    my_queue.put('world')
    ans3 = my_queue.queue[0]  # 引用[0]的值，但不取出
    lens = len(my_queue.queue)
    print(lens)
    print(ans3)
    """empty() -- 檢查queue是否是空的"""
    print('\nPart 4')
    my_queue = queue.Queue()
    try:
        item = my_queue.get_nowait()
    except queue.Empty:
        print('Queue Empty')
