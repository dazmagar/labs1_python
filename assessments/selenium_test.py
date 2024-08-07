import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class MainTest:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def main_method(self) -> dict:
        self.driver.get(url="https://www.saucedemo.com/")

        # Fetch the usernames and passwords displayed on the page
        usernames_element = self.wait.until(ec.presence_of_element_located((By.ID, "login_credentials")))
        usernames = usernames_element.text.split(":")[1].strip().split("\n")

        password_element = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "login_password")))
        password = password_element.text.split(":")[1].strip()

        # Enter the details in the login form and click on the login button
        time.sleep(3)
        self.driver.find_element(By.ID, "user-name").send_keys(usernames[0])  # Use the first username
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        # Fetch the title of the login page and store it in login_header
        usernames_element = self.wait.until(ec.presence_of_element_located((By.ID, "header_container")))
        login_header = self.driver.title

        # Fetch the titles of the first five products displayed on the login page
        product_titles = [element.text for element in self.wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))[:5]]

        data = {"usernames": usernames, "password": password, "login_header": login_header, "product_titles": product_titles}

        time.sleep(3)
        self.driver.quit()
        return data


if __name__ == "__main__":
    test = MainTest()
    print(test.main_method())
