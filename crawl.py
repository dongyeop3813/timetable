import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import json
from variable import *
from parse import parse_raw

your_id = "[depracated]"
your_pwd = "[depracated]"


def recieve_lecture_inform(id, pwd):

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(url=POVIS_URL)

    # login for povis portal
    driver.find_element(By.ID, "login_id").send_keys(id)
    pwd_box = driver.find_element(By.ID, "login_pwd").send_keys(pwd)
    driver.find_element(
        By.XPATH,
        '//input[@type="button"]',
    ).click()

    # open lecture inform tab
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "proceed-button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "navNode_1_2").click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "navNodeAnchor_2_2").click()
    driver.switch_to.frame("ivuFrm_page0ivu2")
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "개설교과목정보조회").click()
    driver.implicitly_wait(10)
    driver.switch_to.frame("ivuFrm_page0ivu0")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "WD1F").send_keys("2022")
    time.sleep(1)

    driver.find_element(By.ID, "WD4E").send_keys("1학기")
    time.sleep(1)

    # crawling the lecture information data
    for depart, code in zip(departments_kr, departments):
        li_list = []
        time.sleep(1)
        driver.find_element(By.ID, "WD74").send_keys(depart)
        time.sleep(3)
        driver.find_element(By.ID, "WDB8").click()
        time.sleep(15)

        table = driver.find_element(By.ID, "WDBF-contentTBody")

        row = table.find_elements(By.TAG_NAME, 'tr')
        for r in row[1:]:
            temp = {}
            col = r.find_elements(By.TAG_NAME, 'td')
            lecture_data = parse_raw(col)
            if "lab" in lecture_data:
                li_list[-1]["lab"] = lecture_data["lab"]
            else:
                li_list.append(lecture_data)

        with open(f"{code}.json", "w") as json_file:
            json.dump(li_list, json_file)

    driver.quit()
    return li_list


if __name__ == "__main__":
    recieve_lecture_inform(id=your_id, pwd=your_pwd)
