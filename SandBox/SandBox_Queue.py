import queue

my_queue = queue.Queue()

# 试图使用get_nowait()方法在队列为空时取出数据
try:
    item = my_queue.get_nowait()
except queue.Empty:
    print("队列为空，无法取出数据")
