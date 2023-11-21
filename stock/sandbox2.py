# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

keywords = "塑膠"
n = '1'
chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                  AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }

# url = 'https://www.google.com/search?q='+keywords+'&oq='+keywords+'&aqs=chrome.0.69i59i450.936026j0j7&sourceid=chrome&ie=UTF-8'
url = 'https://www.google.com/search?q=' + keywords + '&ei=' + keywords + 'hTKhY8SpFdjZhwPAnqWQDQ&start=' + n + '0&sa=N&ved=2ahUKEwiEgI3ppof8AhXY7GEKHUBPCdI4ChDy0wN6BAgFEAQ&biw=1920&bih=969&dpr=1'
url2 = 'https://www.google.com/search?q=' + keywords + '&ei=' + keywords + 'KDKhY5mpL7vc2roPuJGV8Ak&start=' + n + '0&sa=N&ved=2ahUKEwiZ3fq8pof8AhU7rlYBHbhIBZ4Q8tMDegQIBhAE&cshid=1671508537243994&biw=1920&bih=969&dpr=1'

html = requests.get(url, headers=chrome_headers)

soup = BeautifulSoup(html.text, 'html.parser')

tags = soup.find_all('div', class_='kvH3mc BToiNc UK95Uc')

rows = []
for tag in tags:
    row = []

    title = tag.find('h3', class_='LC20lb MBeuO DKV0Md')
    row.append(title.text)
    print(title.text)

    descripe = tag.find('div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf')
    row.append(descripe.text)
    print(descripe.text)

    link = tag.find('a')
    row.append(link.get('href'))
    print(link.get('href'))

    time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    row.append(time)
    print(time)

    rows.append(row)

with open('10810306_google_search_p' + n + '.csv', 'w', newline='', encoding='utf-8-sig') as savefile:
    data = csv.writer(savefile)
    data.writerow(['標題', '描述', '超連結', '抓取時間'])
    for row in rows:
        data.writerow(row)

    print(row[0] + '\n' + row[1] + '\n' + row[2] + '\n' + row[3])
    print(rows)