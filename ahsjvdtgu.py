from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By
import pytest


driver: WebDriver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")


def login():
    driver.get("https://resume-filter-frontend-urtjok3rza-wl.a.run.app/login")
    driver.find_element(By.XPATH, '//*[@id="emailAddress"]').send_keys("HR")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('yashas@1952000')
    driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div[2]/div[2]/div/div/div/div/form/div[4]').click()
    time.sleep(5)
    assert driver.find_element(By.XPATH,value="/html/body/app-root/app-dashboard/div/div[1]/div[1]").is_displayed() == True
    print("login successfull")
    time.sleep(5)
    driver.find_element(By.XPATH, value="//a[@class='nav-link']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys("the")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="inputEmail"]').send_keys('QA')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="inputSkills"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="inputSkills"]').send_keys("C,C++,CSS,HTML")
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="expert"]').click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR,'#expert').click()
    driver.find_element(By.CSS_SELECTOR,'#expert > option:nth-child(24)').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,'#inputStartDate').send_keys("04/19/2022")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#inputEndDate').send_keys("04/19/2022")
    time.sleep(15)
    drp = driver.find_element(By.CSS_SELECTOR,"#resumes")
    drp.send_keys("C:\\Users\\dryashas\\Downloads\\Resumes.zip")
    time.sleep(5)
    # driver.find_element(By.XPATH," //button[@type='submit']").click()
    # print("Recruitment successfully added")
    driver.find_element(By.CSS_SELECTOR,'body > app-root > app-add-recruitment > div.col-md-6.offset-md-3.mt-5.container > form > div.container-fluid.mt-5.buttons > button:nth-child(1) > u').click()
    print("Reset performed, fill the details")

login()
# driver.close()
