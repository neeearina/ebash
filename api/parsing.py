from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from data import __all_models, db_session
from data.category_table import Category
from data.prof_in_cat import Proff
import requests
import json


def append_to_db_category(name):
    try:
        db_sess = db_session.create_session()  # подключаемся к бд
        obj = Category()
        obj.name_c = name
        db_sess.add(obj)
        db_sess.commit()
    except Exception as e:
        print(e)


cat_all = []


#
# cat_all = ['https://www.profguide.io/professions/category/medicine/',
#            'https://www.profguide.io/professions/category/it/',
#            'https://www.profguide.io/professions/category/designe/',
#            'https://www.profguide.io/professions/category/managment/',
#            'https://www.profguide.io/professions/category/kino_teatr/',
#            'https://www.profguide.io/professions/category/ingenire/',
#            'https://www.profguide.io/professions/category/transport/',
#            'https://www.profguide.io/professions/category/marketing/',
#            'https://www.profguide.io/professions/category/science/',
#            'https://www.profguide.io/professions/category/pedagogy/',
#            'https://www.profguide.io/professions/category/smi/',
#            'https://www.profguide.io/professions/category/finansi/',
#            'https://www.profguide.io/professions/category/jurist/',
#            'https://www.profguide.io/professions/category/serice_turism/',
#            'https://www.profguide.io/professions/category/sportBeauty/',
#            'https://www.profguide.io/professions/category/stroitelstvo/',
#            'https://www.profguide.io/professions/category/professions_in_sports/',
#            'https://www.profguide.io/professions/category/lightprom/',
#            'https://www.profguide.io/professions/category/food/',
#            'https://www.profguide.io/professions/category/trade/',
#            'https://www.profguide.io/professions/category/veterinar/',
#            'https://www.profguide.io/professions/category/heavy_industry/',
#            'https://www.profguide.io/professions/category/geologia/',
#            'https://www.profguide.io/professions/category/sil_structur/',
#            'https://www.profguide.io/professions/category/sekretariat/',
#            'https://www.profguide.io/professions/category/politika/',
#            'https://www.profguide.io/professions/category/show-biz/']


def add_to_db_prof(id_cat, name_p, zp, discr):
    try:
        db_sess = db_session.create_session()  # подключаемся к бд
        obj = Proff()
        obj.id_category = id_cat
        obj.name = name_p
        obj.zarplata = zp
        obj.description = discr
        db_sess.add(obj)
        db_sess.commit()
    except Exception as e:
        print(e)


def find_pfofessions():
    id_cat = 0
    try:
        for url in cat_all:
            id_cat += 1
            service = Service(executable_path='C:/chromedriver/chromedriver')
            browser = webdriver.Chrome(service=service)
            browser.get(url)
            time.sleep(2)
            cont_with_category = browser.find_element(By.CLASS_NAME, 'grid-view')
            sp_prof = cont_with_category.find_elements(By.TAG_NAME, 'tr')
            for el in sp_prof:  # по порядку контейнеры с инф о каждой профессии
                inf_prof = el.find_elements(By.TAG_NAME, 'td')
                if len(inf_prof) < 3:
                    pass
                else:
                    name = inf_prof[0].text
                    zp = inf_prof[1].text
                    discr = inf_prof[2].text
                    add_to_db_prof(id_cat, name, zp, discr)
            print(url, id_cat)
    except Exception as e:
        print(e)


def selenium_find_category():
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
            for_s = el.find_element(By.TAG_NAME, 'a')
            sorce = for_s.get_attribute('href')  # ссылка на категорию
            cat_all.append(sorce)
            append_to_db_category(name)
        time.sleep(1)
        browser.quit()
        find_pfofessions()
    except Exception as e:
        print(e)
        browser.quit()

# selenium_find_category()
