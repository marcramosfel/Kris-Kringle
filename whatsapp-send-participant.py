from selenium import webdriver

# Replace 'my-phone-number' with your phone number (including the country code)
driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/send?phone=my-phone-number')

# Wait for the page to load
input('Press enter after scanning the QR code')

# Find the chat box and the send button
chat_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')

# Type the message in the chat box and click the send button
chat_box.send_keys('Hello, this is an automated message!')
send_button.click()

# Close the browser
driver.quit()
