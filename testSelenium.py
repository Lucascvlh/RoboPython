from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://kirk.magazineluiza.com.br/')
driver.find_element_by_xpath(
    '//*[@id="identifier"]').send_keys('luch_carvalho')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Lu180513!')
driver.find_element_by_xpath(
    '/html/body/div[1]/div/view-sign-in/component-card/form/div[2]/button').click()
sleep(5)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[4]/view-services/super-bar/div/component-search/button').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[4]/view-services/super-bar/div/component-search/input').send_keys('soft')
sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[4]/view-services/div[2]/div/div[2]/a/component-card/div[1]').click()
sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/component-dialog-container/component-dialog/div/component-card/div/form/div[2]/button[1]').click()
go
