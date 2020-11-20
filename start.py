from time import sleep, time
from selenium import webdriver
from datetime import datetime
from setting import TOKEN
from pprint import pprint

now = datetime.now()

start_time = now.strftime("%H:%M")
start_min = int(now.strftime("%M"))


print("start Time =", start_time)

driver = webdriver.Chrome('./web-driver/chromedriver')
driver.maximize_window()
driver.get('https://shopee.co.id/')
driver.add_cookie({'name': 'SPC_EC', 'value': TOKEN})

sleep(.2)
csrf = driver.get_cookies()
# pprint(csrf)

url_prod = "https://shopee.co.id/NA-Peniti-SWAN-isi-12-pcs-Peniti-Hijab-Peniti-Jilbab-Peniti-Set-i.3188474.2830283548"
driver.get(url_prod)

sleep(1)
btn_buy = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]').click()
driver.get('https://shopee.co.id/cart/')

sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/label').click()

# sleep(1)
while True:

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    end = now.strftime("%H")
    end_time = start_min + 2
    sleep(1)
    print("Current Time =", current_time)
    if start_time == "{}:{}".format(end,end_time):
        xpath = '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button'
        btn_checkout = driver.find_element_by_xpath(xpath).click()
        print("Checkout")
        print("End Time =", current_time)
        break;


    
# driver.get('https://shopee.co.id/checkout')

# driver.close()

