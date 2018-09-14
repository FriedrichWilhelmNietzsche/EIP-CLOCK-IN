#! /usr/bin/env python
# -*- coding: utf-8 -*-

# NuEIP clock in and clock out

from selenium import webdriver
import time
import datetime



def doSth():
    print('start')
    driver = webdriver.Chrome()
    driver.get("https://cloud.nueip.com/login")
    time.sleep(3)
    # F12, find_element_by_xpath\ css_selector()
    driver.find_element_by_xpath(' //*[@id="dept_input"] ').send_keys("dps")
    driver.find_element_by_xpath(' //*[@id="username_input"] ').send_keys("d0049")
    driver.find_element_by_xpath(' //*[@id="password_input"] ').send_keys("David123")
    driver.find_element_by_xpath(' //*[@id="login-button"]  ').click()   # login
    time.sleep(6)
    driver.find_element_by_xpath(' //*[@id="mm-0"]/div[5]/div/div[1]/div[5]/div[1]/div/div[2]/div/div[1]/div ').click()  # clock in
    time.sleep(6)
    driver.find_element_by_xpath(' //*[@id="mm-0"]/div[3]/div/div[1]/div[5]/div[1]/div/div[2]/div/div[2]/div ').click()  # clock out
    time.sleep(6)



# set login time
def main(h=17, m=42):
    while True:
        now = datetime.datetime.now()
        print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            break

        time.sleep(60)
    doSth()

main()


# F12, find_element_by_id\ name()\ class_name()\ tag_name()\<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# driver.find_element_by_id("kw").send_keys("test")
# find_element_by_link_text\ partial_link_text()
# driver.find_element_by_link_text("登录").click()




