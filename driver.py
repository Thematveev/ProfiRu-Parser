from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from config_reader import get_credentials

from time import sleep
import re


username, password = get_credentials()

class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        # self.driver.minimize_window()
        print("Driver started.")

    def login(self):
        print("Trying to login...")
        self.driver.get('https://profi.ru/backoffice/n.php')
        try:
            authblock = self.driver.find_element(By.CLASS_NAME, 'auth-container')
        except NoSuchElementException:
            authblock = None

        if authblock is not None:
            login = self.driver.find_element(By.CLASS_NAME, 'login-form__input-login')
            login.send_keys(username)
            pwd = self.driver.find_element(By.CLASS_NAME, 'login-form__input-password')
            pwd.send_keys(password)
            enterBtn = self.driver.find_element(By.CLASS_NAME, 'login-form__button')
            sleep(2)
            enterBtn.click()
            print("Logged in!")

    def parseOrders(self):
        print("Parsing started...")
        sleep(10)
        self.driver.refresh()
        sleep(10)
        result = []
        orders = self.driver.find_elements(By.CLASS_NAME, 'OrderSnippetContainerStyles__Container-sc-85p0ef-0')
        for order in orders:
            title = order.find_element(By.CLASS_NAME, 'SubjectAndPriceStyles__SubjectsText-xoorkf-1').text
            price = order.find_element(By.CLASS_NAME, 'SubjectAndPriceStyles__PriceValue-xoorkf-5').text
            date = order.find_element(By.CLASS_NAME, 'Date__DateText-sc-110ytd8-1').text
            link = order.find_element(By.TAG_NAME, 'a').get_attribute('href')
            id = re.search('o=[0-9]*', link).group(0)[2:]
            result.append({
                "id": id,
                "title": title,
                "price": price,
                "date": date,
                "link": link
            })
        print("Parsing finished...")
        return result


