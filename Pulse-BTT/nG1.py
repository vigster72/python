from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = '/usr/bin/chromedriver'
browser = webdriver.Chrome(driver)
browser.get('https://172.23.246.11/racommon/NSLogin.jsp?redirect=/console')

username = chromedriver.find_element_by_name("usernameText")
password = chromedriver.find_element_by_name("passwordText")

username.send_keys("jvigliotti")
password.send_keys("Bat#cave0220")

chromedriver.find_element_by_id("submitBtn").click()



















