from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the web driver
driver = webdriver.Chrome('/Users/jonathanhsu/Downloads/chromedriver')

# Navigate to the website
driver.get('https://sports.ny.betmgm.com/en/sports/football-11/betting/usa-9/nfl-35')

# Wait 5 seconds
driver.implicitly_wait(1)

# Locate all elements with the "div" tag, "class" attribute name, and "participant" attribute value
elements = driver.find_element(By.XPATH,"//div[@class='participant']")

# Get the text attribute and print it
for element in elements:
  print(element.text)

# Close the web driver
driver.quit()