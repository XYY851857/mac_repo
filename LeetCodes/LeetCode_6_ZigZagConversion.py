# 字串"PAYPALISHIRING"經過Z字轉換後如圖所示，重組後變成"PAHNAPLSIIGYIR"， 寫一個convert(string text, int nRows)來將傳入的字串text轉換成n行的Z字轉換。
# convert("PAYPALISHIRING", 3) 會回傳 "PAHNAPLSIIGYIR"。
# 這邊用另外一個範例來解釋會比較清楚：
# text = "ABCDEFGHIJKLMN", n = 4，排成Z字如下，因此轉換後的字串為 "AGMBFHLNCEIKDJ"
# A     G     M
# B   F H   L N
# C E   I K
# D     J


def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ['' for _ in range(numRows)]

    current_row, direction = 0, 1

    for char in s:
        rows[current_row] += char
        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1
        current_row += direction

    result = ''.join(rows)

    return result



if __name__ == "__main__":
    input_str = ("ABCDEFGHIJKLMN")
    num_rows = 3
    result = convert(input_str, num_rows)
    print(result)
