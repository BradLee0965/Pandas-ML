import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://naver.com/')
time.sleep(5)
print(driver.title)
print(driver.current_url)
# driver.find_element_by_xpath("//*[@id=\"container\"]/main/div/div[2]/div[2]/div/figure[2]/span/img").click()
driver.find_element_by_class_name('link_login').click()
time.sleep(4)
driver.find_element_by_name('id').send_keys('colorduo')
time.sleep(10)
driver.find_element_by_name('pw').send_keys('@tmdgh64300965')
time.sleep(4)
driver.find_element_by_class_name('btn_login').click()
time.sleep(5)
driver.quit() # driver.close() 쓰면 ImportError: sys.meta_path is None, Python is likely shutting down 뜸.


