from selenium import webdriver

driver_path = 'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.example.com/login")

# Find the username and password fields and fill them out
username_field = driver.find_element("name", "username")
password_field = driver.find_element("name", "password")

username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Submit the form
password_field.submit()

# Close the browser window
driver.quit()
