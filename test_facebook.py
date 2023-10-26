from time import sleep

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

cService = webdriver.ChromeService(executable_path=r'C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=cService)

@pytest.fixture
def default():
    print(" once before testmethod execution")
    yield
    print(" once after testmethod execution")


def testm1(default):
    print("test1")
    driver.get("https://rvm1.epizy.com/?i=1")
    sleep(5)
    driver.find_element(By.LINK_TEXT, "Sign Up").click()


def testm2(default):
    print("test2")
    driver.find_element(By.ID, "Username").send_keys("he123")
    driver.find_element(By.ID, "psw").send_keys("he1234")
    driver.find_element(By.ID, "Re_enter_Password ").send_keys("he1234")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()

