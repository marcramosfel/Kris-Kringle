from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Replace 'my-phone-number' with your phone number (including the country code)
driver = webdriver.Chrome('.chromedriver')
driver.get('https://web.whatsapp.com/send?phone=+351961473869')
wait = WebDriverWait(driver, 100)
# Wait for the page to load
# input('Press enter after scanning the QR code')
driver.implicitly_wait(15)

# Find the chat box and the send button

chat_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
chat_box = driver.find_element(by=By.XPATH, value=chat_box_path)
# Type the message in the chat box and click the send button

text = 'Hello, this is an automated message! Voce e o amor da minha vida!' 

chat_box.send_keys(text + Keys.ENTER)

