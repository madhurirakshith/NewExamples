from selenium import webdriver
from selenium.webdriver.common.keys import Keys
qspiders=webdriver.Chrome(executable_path=("C:/Users/Rakshith Yenadka/Downloads/chromedriver_win32/chromedriver.exe"))
qspiders.get("http://www.google.com")
qspiders.find_element_by_name('q').send_keys("testing")
qspiders.find_element_by_name('q').send_keys(Keys.ENTER)