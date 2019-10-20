from splinter import Browser
from time import sleep

username = 'YOUR_USERNAME_HERE'
password = 'YOUR_PASSWORD_HERE'
#url = 'https://kissanime.ru/Anime/Yahari-Ore-no-Seishun-Love-Comedy-wa-Machigatteiru-Zoku'
#url = 'https://kissanime.ru/Anime/Hinamatsuri'
url = 'https://kissanime.ru/Anime/The-Legend-of-Korra'

browser = Browser('chrome') # defaults to firefox
browser.visit('https://kissanime.ru/Login')
sleep(8)
window = browser.windows[0]
browser.fill('username', username)
browser.fill('password', password)
browser.find_by_id('btnSubmit').click()
window.close_others()
browser.visit(url)
sleep(3)
links = []
for i in range(1,30):
	try:
		print(i)
		link = browser.find_by_xpath('//*[@id="leftside"]/div[2]/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[1]/a')['href']
		if 'episode' in link.lower():
			links.append(link)
	except Exception:
		if len(links) > 0:
			break
		else:
			pass
print(links)
downloads = []
for l in links:
	browser.visit(l)
	browser.find_by_xpath('//*[@id="formVerify1"]/div[3]/p[1]/a').click()
	sleep(1)
	print('closing other windows')
	window.close_others()
	browser.visit(browser.find_by_xpath('//*[@id="divDownload"]/a')['href'])
	dlnk = browser.find_by_xpath('//*[@id="button-download"]').last['href']
	if not '720.mp4' in dlnk:
		print('not 720p mp4', l)
	else:
		downloads.append(dlnk)
print(downloads)
for d in downloads:
	browser.visit(d)
	sleep(1)
