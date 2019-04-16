from splinter import Browser
from time import sleep

username = 'origamimaster951'
password = 'Origami123'
url = 'https://kissanime.ru/Anime/Yahari-Ore-no-Seishun-Love-Comedy-wa-Machigatteiru-Zoku'

browser = Browser('chrome') # defaults to firefox
browser.visit('https://kissanime.ru/Login')
sleep(10)
window = browser.windows[0]
browser.fill('username', username)
browser.fill('password', password)
browser.find_by_id('btnSubmit').click()
browser.visit(url)
sleep(20)
browser.quit()
'''
browser.visit(url)
sleep(100)
for i in range(1,10)
	print(browser.find_by_xpath('//*[@id="leftside"]/div[2]/div[2]/div[2]/table/tbody/tr['+i+']/td[1]/a').href)
browser.quit()
'''