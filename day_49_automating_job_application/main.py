from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

user_email = "usermail@outlook.com"
user_password = "1122323"

service = Service("./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3479417900&f_LF=f_AL&geoId=102105699&keywords=Python%20Developer&location=T%C3%BCrkiye&refresh=true")

driver.find_element(By.XPATH, "//div/a[@class='nav__button-secondary btn-md btn-secondary-emphasis']").click()

driver.find_element(By.ID, "username").send_keys(user_email)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(user_password)
password_input.submit()

time.sleep(2)
job_list = driver.find_elements(By.CLASS_NAME, "job-card-container")
time.sleep(2)

for i in range(len(job_list)):
    job_list[i].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='jobs-apply-button--top-card']/button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
    driver.find_element(By.XPATH, "//div/button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
    driver.find_element(By.XPATH, "//div/button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
