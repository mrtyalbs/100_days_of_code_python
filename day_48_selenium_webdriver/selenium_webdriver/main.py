from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

view_history = driver.find_element(By.LINK_TEXT, "View history")
# view_history.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("earthquake engineering", Keys.ENTER)



# driver.quit()