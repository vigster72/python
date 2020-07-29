from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=Googlebot/2x")
#driver = webdriver.Chrome(chrome_options=opts)
#import XPATH
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome('/usr/bin/chromedriver', 'chrome_options=opts')
driver = webdriver.Chrome(chrome_options=opts)
driver.get("https://www.costcobusinessdelivery.com")
print(driver.title)
#WebDriverWait = ''
# Find login/signin
login_button = driver.find_element_by_xpath("//*[@id='header_sign_in']")
#login_button = driver.find_element_by_xpath('/html/body/header/div[2]/div/div/div[2]/div[2]/div/div[3]/ul/li[2]/a')
# Click login - #myaccount-m > span
login_button.click()
agent = driver.execute_script("return navigator.userAgent")
print(agent)
#login_button.submit()
#//*[@id="header_sign_in"]
#driver.find_element_by_id("header_sign_in").click()
#username = driver.find_element_by_name("logonId")
#password = driver.find_element_by_name("logonPassword")

#username.send_keys("jvigliotti")
#password.send_keys("Bat#cave0220")

#driver.find_element_by_id("submitBtn").click()

#driver.find_element_by_xpath(),e#driver.find_elem
#driver.find_element_by_xpath("//div[text()='Service Dashboard']//parent::button").click()
#WebDriverWait(driver, 20).until(ExpectedConditions.elementToBeClickable(By.xpath("//button[@class='module' and text()='Dashboards'][@data-ember-