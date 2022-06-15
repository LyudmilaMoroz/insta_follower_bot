from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.driver_path = Service(chrome_driver_path)
        self.op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.driver_path, options=self.op)

    def accept_cookies(self):
        self.driver.get("https://www.instagram.com/")
        accept_button = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        accept_button.click()
        time.sleep(5)

    def login(self, username, password):
        username_input = self.driver.find_element(By.CLASS_NAME, "f0n8F")
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        time.sleep(10)

    def find_followers(self, similar_account):
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        time.sleep(5)
        n = self.driver.find_elements(By.CLASS_NAME, 'g47SY')
        followers = self.driver.find_element(By.LINK_TEXT, f'{n[1].text} подписчиков')
        followers.click()
        time.sleep(5)
        # scroll_element = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
        #     time.sleep(2)
        scroll = True
        while scroll:
            scroll_element = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
            scroll_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_element)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
            time.sleep(2)
            scroll_height_new = self.driver.execute_script("return arguments[0].scrollHeight", scroll_element)
            if scroll_height_new == scroll_height:
                scroll = False
            time.sleep(2)

    def follow(self):
        buttons_list = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in buttons_list:
            print(button.text)
            if button.text == "Подписаться":
                button.click()
                time.sleep(5)
