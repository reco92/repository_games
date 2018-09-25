import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from constants import URL

path = os.path.dirname(os.path.abspath(__file__))

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(
    executable_path='{paht}/../statics/chromedriver'.format(paht=path),
    chrome_options=option)
# drive = webdriver.Firefox('{paht}/../statics/geckodriver'.format(paht=path))
browser.get(URL)
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#games-list-container > ul")
        )
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

games = browser.find_elements_by_css_selector("#games-list-container > ul li")
# games_titles = []
for game in games:
    title = game.find_element_by_tag_name('h3').text
    print('title:', title)

browser.close()

#games-list-container > ul > li:nth-child(1)
#games-list-container > ul

###LINKS:
#https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
#https://selenium-python.readthedocs.io/locating-elements.html