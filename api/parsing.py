from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request

from data import __all_models, db_session
from data.category_table import Category


def append_to_db(name):
    try:
        print(name)
        print(type(name))
        db_sess = db_session.create_session()  # подключаемся к бд
        obj = Category()
        obj.name_c = name
        db_sess.add(obj)
        db_sess.commit()
    except Exception as e:
        print(e)


def selenium_find():
    try:
        url = 'https://www.profguide.io/professions/'
        service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
        browser = webdriver.Chrome(service=service)
        browser.get(url)
        time.sleep(2)
        cont_with_category = browser.find_element(By.CLASS_NAME, 'list-prof-cat')  # находим класс со списком
        sp_cat = cont_with_category.find_elements(By.TAG_NAME, 'li')
        for el in sp_cat:
            name = el.find_element(By.TAG_NAME, 'a').text
            append_to_db(name)
        time.sleep(3)
        browser.quit()
    except Exception as e:
        print(e)
        browser.quit()
        return None

