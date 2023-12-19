from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

element = driver.find_element(By.ID, '')  # 需要import from selenium.webdriver.common.by import By

elements = driver.find_elements(By.CLASS_NAME, '')  # 尋找所有匹配的元素，以「列表形式返回」

input_box = driver.find_element(By.NAME,'username')  # 用於輸入框輸入文本
input_box.send_keys('your_username')

submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()  # 用於點擊頁面上的按鈕或連結

input_box = driver.find_element(By.NAME, 'username')  # 用於清除輸入框中的文本
input_box.clear()

element= driver.find_element(By.ID, 'element_id')  # 獲取元素的屬性值
value = elements.get_attribute('attribute_name')

element = driver.find_element(By.XPATH, '')  # 獲取元素的可見文本
value = element.text

element = driver.find_element(By.ID, 'element_id')  # 檢查元素是否可見
if element.is_displayed():
    print('Element is visible')

element = WebDriverWait(driver, 10).until(  # WebDriverWait: 用於等待特定條件的元素出現，以解決異步加載的問題。
    EC.pressence_of_element_located((By.ID, ''))  # 需要import
)



