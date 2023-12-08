list1 = ["3000", "16%", "4000", "50%"]
for one in range(0, len(list1), 2):
    ans1, ans2 = list1[one], list1[one+1]
    print(f'ans1 = {ans1}, ans2 = {ans2}, one = {one}')