from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

import time
import socket


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"C:\Windows\geckodriver.exe")
        # self.driver = webdriver.Firefox(executable_path=r'C:\Users\luane\OneDrive\Área de Trabalho\geckodriver\geckodriver.exe')
        # self.driver = webdriver.Firefox(executable_path=r'C:\Users\luane\OneDrive\Área de Trabalho\geckodriver\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        try:
            login_button = driver.find_element(By.XPATH, "//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        user_element = driver.find_element(By.XPATH, "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element(By.XPATH, "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)


robozin = InstagramBot('TESTE', 'TESTE2')
robozin.login()
