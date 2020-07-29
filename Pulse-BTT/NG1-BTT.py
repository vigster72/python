from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import XPATH
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://172.23.246.11/racommon/NSLogin.jsp?redirect=/console")
print(driver.title)
WebDriverWait = ''
#username = driver.find_element_by_name("displayUsername")
#password = driver.find_element_by_name("displayPassword")

#username.send_keys("jvigliotti")
#password.send_keys("Bat#cave0220")

#driver.find_element_by_id("submitBtn").click()

#driver.find_element_by_xpath(),e#driver.find_elem
#driver.find_element_by_xpath("//div[text()='Service Dashboard']//parent::button").click()
#WebDriverWait(driver, 20).until(ExpectedConditions.elementToBeClickable(By.xpath("//button[@class='module' and text()='Dashboards'][@data-ember-action]"))).click();