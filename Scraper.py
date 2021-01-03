from selenium import webdriver
import csv
import time

URL = 'https://forum.level1techs.com/'
PATH = 'M:\Programming\Python Support Files\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

#infinite scroller from: https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
driver.get(URL)
time.sleep(2)
scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1
scrolls = 0

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    scrolls += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height or scrolls == 2: #limits scrolls
        break

posts = driver.find_elements_by_class_name('topic-title')
views_replies = driver.find_elements_by_class_name('number')

#cuts out pinned posts
del posts[:2]
del views_replies[:4]


for t in posts:
    print(t.text)
for t in views_replies:
    print(t.text)

#removes k
for t in views_replies:

views = []
replies = []
for n in views_replies

with open('data.csv', mode='w') as csv_file:
    fieldnames = ['post name', 'views', 'replies']
    data_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    data_writer.writeheader()
    data_writer.writerow()




