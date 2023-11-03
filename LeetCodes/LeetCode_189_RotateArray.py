# https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/189md.html
# 給一個n值，n代表陣列中包含1~n個元素與一個整數k，將陣列裡面的元素向右旋轉k次。
#
# 範例：
# n=7,k=3, array[1,2,3,4,5,6,7] -->  [5,6,7,1,2,3,4]


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    lens = len(array)
    times = 4
    for i in range(times):
        array.insert(0, array.pop())
    print(array)

