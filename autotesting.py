from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://todomvc.com/examples/react/#/')
searchbox = driver.find_element_by_xpath('/html/body/section/div/header/input')
searchbox.send_keys('a'u'\ue007'u'b'u'\ue007'u'c'u'\ue007')

bbutton = driver.find_element_by_xpath('/html/body/section/div/section/ul/li[2]/div/input')
bbutton.click()

import time
time.sleep(2)
activebutton = driver.find_element_by_xpath('/html/body/section/div/footer/ul/li[2]/a').click()

time.sleep(2)
compbutton = driver.find_element_by_xpath('/html/body/section/div/footer/ul/li[3]/a').click()