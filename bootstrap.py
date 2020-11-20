from selenium import webdriver
from time import sleep
from setting import (TOKEN, PRODUCT_URL)


class App:
    def __init__(self, token, product_url):
        options = webdriver.ChromeOptions().add_argument("headless")
        self.driver = webdriver.Chrome(
            './web-driver/chromedriver', options=options)
        self.url = product_url
        self.token = token

    def prepare(self):
        self.driver.get('https://shopee.co.id/')
        self.driver.add_cookie({'name': 'SPC_EC', 'value': self.token})

        # Go to targeted Product
        self.driver.get(self.url)

        # Get Username
        self.user = self.driver.execute_script(
            "return localStorage.getItem('username')")
        print("[X] LOGIN SUCCESS AS :", self.user)

    def get_item(self):
        # Get Product name
        product_name = self.driver.title.split('|')[0]

        # Add Product to cart
        self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]').click()
        self.driver.get('https://shopee.co.id/cart/')
        print(f"[X] Add to cart : {product_name} ")

    def count_down(self, fun):
        pass

    def checkout(self, fun):
        pass

    def run(self):
        self.prepare()
        sleep(.1)
        self.get_item()
        sleep(5)
        self.done()
        # pass

    def done(self):
        self.driver.close()
        print("[X] Done All")
        pass


app = App(token=TOKEN, product_url=PRODUCT_URL).run()
