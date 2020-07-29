from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/bin/chromedriver')
#browser = webdriver.Chrome(chromedriver)
driver.get('https:\\www.wikipedia.com')

# Find search dialog box
search_box = driver.find_element_by_id('searchInput')
# Send search input
search_box.send_keys('NetScout')
# Find search button
search_button = driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button/i')
# Click login
search_button.click()
search_box1 = driver.find_element_by_id('searchInput')
search_box1.send_keys('NasDaq')
# Find search button
search_button2 = driver.find_element_by_id('searchButton')
# Click login #searchButton
search_button2.click()
driver.close()
#username = selenium.find_element_by_id("username")
#password = selenium.find_element_by_id("password")

#username.send_keys("YourUsername")
#password.send_keys("Pa55worD")

#selenium.find_element_by_name("submit").click()