from selenium import webdriver

# Specify the path to your WebDriver executable
driver_path = 'path/to/chromedriver.exe'  # Update this with the path to your WebDriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open a website
driver.get("https://www.youtube.com")

# Close the browser window
driver.quit()
