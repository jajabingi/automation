from selenium import webdriver

driver_path = 'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.example.com")

# Click on an element
link = driver.find_element("link text", "Click me")
link.click()

# Close the browser window
driver.quit()
