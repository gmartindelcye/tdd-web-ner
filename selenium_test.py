import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService

options = webdriver.FirefoxOptions()
options.set_capability("loggingPrefs", {'performance': 'ALL'})
service = FireFoxService(executable_path='/usr/bin/geckodriver' )
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://www.google.com")

time.sleep(10)

driver.close()