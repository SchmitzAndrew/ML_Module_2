from selenium import webdriver
import csv
import time

URL = 'https://forum.level1techs.com/'
PATH = 'M:\Programming\Python Support Files\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# infinite scroller from: https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
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
    if (screen_height) * i > scroll_height or scrolls == 2:  # limits scrolls
        break

posts = driver.find_elements_by_class_name('topic-title')
replies_views = driver.find_elements_by_class_name('number')

# cuts out pinned posts
del posts[:2]
del replies_views[:4]

#makes posts text
cleaned_posts = []
for t in posts:
    cleaned_posts.append(t.text)

#makes list of only text
replies_views_text = []
for t in replies_views:
    replies_views_text.append(t.text)

# removes k
cleaned_replies_views = []
for n in replies_views_text:
    if "k" in n:
        n = n.replace('k', '')
        n = float(n) * 1000
        n = int(n)
        n = str(n)
        cleaned_replies_views.append(n)
    else:
        cleaned_replies_views.append(n)



views = []
replies = []
index = 0

for i in cleaned_replies_views:
    if index % 2 == 0:
        replies.append(cleaned_replies_views[index])
    else:
        views.append(cleaned_replies_views[index])
    index += 1


with open('data.csv', mode='w') as csv_file:
    data_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    try:
        data_writer.writerow(cleaned_posts)
    except UnicodeEncodeError:
        pass
    data_writer.writerow(views)
    data_writer.writerow(replies)

print(cleaned_posts)
print(views)
print(replies)

#find reply to view ratio

total_views = 0
for i in views:
    total_views += int(i)
total_replies = 0

for i in replies:
    total_replies += int(i)

view_to_reply = total_views / total_replies
print(view_to_reply)



