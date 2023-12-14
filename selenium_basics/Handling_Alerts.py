from selenium import webdriver

driver_path = 'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.example.com")

# Click on a button that triggers an alert
button = driver.find_element("id", "alertButton")
button.click()

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

# Close the browser window
driver.quit()
