from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By


driver: WebDriver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

def login():
    driver.get("https://resume-filter-frontend-urtjok3rza-wl.a.run.app/user/addrecruitment")
    driver.get("https://resume-filter-frontend-urtjok3rza-wl.a.run.app/login")
    driver.find_element(By.XPATH, '//*[@id="emailAddress"]').send_keys("HR")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('yashas@1952000')
    driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div[2]/div[2]/div/div/div/div/form/div[4]').click()
    time.sleep(5)
    assert driver.find_element(By.XPATH,value="/html/body/app-root/app-dashboard/div/div[1]/div[1]").is_displayed() == True
    print("login successfull")

def start():
    driver.find_element(By.CSS_SELECTOR, value="body > app-root > app-dashboard > div > div.sub-header.container > div.dashboard-dropdowns > div.sort-by > div:nth-child(2) > select").click()
    time.sleep(5)
    # drp.select_by_visible_text('HR')
    driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashboard > div > div.sub-header.container > div.dashboard-dropdowns > div.sort-by > div:nth-child(2) > select > option:nth-child(2)").click()
    print("Sorting by start date successful")


def end():
    driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashboard > div > div.sub-header.container > div.dashboard-dropdowns > div.sort-by > div:nth-child(2) > select").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"body > app-root > app-dashboard > div > div.sub-header.container > div.dashboard-dropdowns > div.sort-by > div:nth-child(2) > select > option:nth-child(3)").click()
    print("Sorting by end date successful")


login()
start()
end()
driver.close()