from selenium import webdriver

driver_path = 'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.example.com")

# Take a screenshot
driver.save_screenshot("screenshot.png")

# Close the browser window
driver.quit()
