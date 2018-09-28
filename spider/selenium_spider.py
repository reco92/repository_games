import os

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from constants import URL

path = os.path.dirname(os.path.abspath(__file__))


def check_exists_by_css(browser, selector):
    """
    Check if a lement exists on the browser

    :param browser: webdriver object
    :param selector: string, css selector

    :return: Boolean
    """

    try:
        browser.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False

    return True



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
games_titles = list()

#do while, if found the button "load more" process the new ones and for not repeat the same save a counter
games = browser.find_elements_by_css_selector("#games-list-container > ul li")

for game in games:
    try:
        title = game.find_element_by_tag_name('h3').text
        sale_price = game.find_element_by_tag_name('s').text
        price = game.find_element_by_class_name('strike').text
        release_date = game.find_element_by_css_selector('p.row-date').text
        release_date = release_date[8:len(release_date)]
        datetime_obj = datetime.strptime(release_date, '%b %d, %Y')

        games_titles.append({
            'title': title,
            'price': price,
            'sale_price': sale_price,
            'date': datetime_obj.date()
        })
    except Exception as excep:
        pass

browser.find_element_by_id('btn-load-more')


print(games_titles)

browser.close()

###LINKS:
#https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
#https://selenium-python.readthedocs.io/locating-elements.html