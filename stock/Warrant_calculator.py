import twstock
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pymongo
from datetime import datetime
from tqdm import tqdm
from pymongo import MongoClient


def get(stock_id):
    # driver = webdriver.Chrome()
    # driver.set_window_size(800, 600)
    # wait = WebDriverWait(driver, 5)
    url = 'https://www.warrantwin.com.tw/eyuanta/Warrant/Search.aspx'
    driver.get(url)

    id_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td/div/input')))  # 股票代號
    id_element.click()  # 股票代號
    id_element.send_keys(stock_id)  # 股票代號
    pc_select_element = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td/div/select')  # 購、售證選單
    maker_select_element = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[3]/td/div/select')  # 造市商選單
    search_element = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[1]/div[1]/div[2]/a[2]')  # 搜尋鈕
    next_page_element = driver.find_element(By.CSS_SELECTOR,'#mm-0 > div.main_block.single > div.main_box > div > div.pagination-container.butM2.ng-isolate-scope > ul > li.PagedList-skipToNext')  # 下一頁按鈕
    maker_dropdown = Select(maker_select_element)  # 造市商選單
    maker_dropdown.select_by_index(0)  # 造市商選單
    pc_dropdown = Select(pc_select_element)  # 購、售證選單
    return_list = []
    for step in 1, 2:
        page_count = 0  # 頁數RESET
        total_volume = 0  # 總交易額RESET
        total_count = 0  # 總筆數RESET
        get_count = 1  # 取得資料數RESET
        pc_dropdown.select_by_index(step)  # 購、售證選單
        search_element.click()  # 搜尋鈕
        time.sleep(0.5)  # 必須設定延遲，可能會因為物件還未改變就被抓去
        total_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[2]/div/p/label[2]'))).text  # 總筆數
        if int(total_count) == 0:
            return "NONE"
        with tqdm(total=int(total_count)) as pbar:
            while (int(total_count) // 20 + 1) != page_count:  # 筆數除以每頁20筆等於總頁數
                field_count = 2  # 欄計數RESET
                turn_volume = 0  # 單頁成交額RESET
                while field_count != 22:
                    value = driver.find_element(By.CSS_SELECTOR, f'#mm-0 > div.main_block.single > div.main_box > div > div:nth-child(4) > div > div.ng-isolate-scope > table > tbody > tr:nth-child({int(field_count)}) > td:nth-child(7) > div').text
                    price = driver.find_element(By.CSS_SELECTOR, f'#mm-0 > div.main_block.single > div.main_box > div > div:nth-child(4) > div > div.ng-isolate-scope > table > tbody > tr:nth-child({int(field_count)}) > td:nth-child(4) > div').text
                    price = price.replace('.', '')
                    if price == '--' or value == '--':
                        field_count += 1
                        if get_count == int(total_count):
                            get_count += 1
                            pbar.update(1)
                            break
                        get_count += 1
                        pbar.update(1)
                        continue
                    turn_volume += int(value) * int(price) * 10
                    field_count += 1
                    if get_count == int(total_count):
                        get_count += 1
                        pbar.update(1)
                        break
                    get_count += 1
                    pbar.update(1)
                    # time.sleep(0.01)
                total_volume += turn_volume
                next_page_element.click()
                time.sleep(0.5)
                page_count += 1
            return_list.append(total_volume)
    # driver.close()
    return return_list


def write(stock_detail, total_volume, price):
    collection = client['warrant_data']['DATA']

    data = {
        f"{(datetime.now()).strftime("%Y%m%d")}": {
            "call": total_volume[0],
            "put": total_volume[1],
            "price": price
        }
    }

    filter = {"_id": f"{stock_detail}"}

    result = collection.update_one(filter, {"$set": data}, upsert=True)
    if result.modified_count > 0 or result.upserted_id:
        print("資料已更新或插入成功")
    else:
        print(f"資料更新或插入失敗\n{result}")


if __name__ == "__main__":
    global driver, client, wait


    def driver_start():
        driver = webdriver.Chrome()  # 實例webdriver
        driver.set_window_size(800, 600)  # 調整視窗大小
        wait = WebDriverWait(driver, 5)
        return driver, wait


    stock_id = None
    while stock_id != 88:
        # stock_id = '6231'
        stock_id = input('INPUT ID: ')
        if stock_id.upper() == 'INDEX' or stock_id.upper() == '$TWT':
            stock_id = '$TWT'
        state1 = stock_id in twstock.twse  # 檢查代號狀態
        state2 = stock_id in twstock.tpex  # 檢查代號狀態
        state3 = stock_id in twstock.codes  # 檢查代號狀態
        if state1 or state2 or state3 or stock_id == '$TWT':
            client = pymongo.MongoClient("mongodb://localhost:27017/")  # 連入伺服器
            if stock_id != '$TWT':
                data = twstock.realtime.get(stock_id)
                stock_detail = data['info']['name']
                print(f"名稱： {stock_detail}")
                driver, wait = driver_start()  # driver！啟動～～
                total_volume = get(stock_id)
                price = f'{float(data['realtime']['latest_trade_price']):.2f}'
                driver.close()
            else:
                stock_detail = '台股指'
                print(stock_detail)
                driver, wait = driver_start()  # driver！啟動～～
                total_volume = get(stock_id)  # GET
                page = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div/a')
                page.click()
                price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#mm-0 > div.main_block.single > div.main_box > div > div.price_box > div:nth-child(1) > p.gray > span:nth-child(4)'))).text
                driver.close()
                print(price)

            if total_volume == "NONE":
                print("未搜尋到相關權證")
                continue
            print(f'股票名稱：{stock_detail} {stock_id}\n購：{total_volume[0]}\n售：{total_volume[1]}')
            write(stock_detail, total_volume, price)  # 寫入資料庫
            # break
    print('break')
