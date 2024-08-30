import os
import time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Define the file paths
message_path = r'E:\\2000\\messege.txt'
numbers_path = r'E:\\2000\\numbers.txt'

# Check if the message file exists
if not os.path.exists(message_path):
    print(f"Error: The file {message_path} does not exist.")
else:
    if not os.path.exists(message_path):
        print(f"Error: The file {message_path} does not exist.")
    else:
        # Read the message from file and URL-encode it
        try:
            with open(message_path, 'r', encoding='utf-8') as file:
                msg = file.read().strip()
        except UnicodeDecodeError:
            print(f"Error: Unable to decode the file {message_path}.")
            exit()

        msg = quote(msg)  # URL-encode the message

    # Check if the numbers file exists
    if not os.path.exists(numbers_path):
        print(f"Error: The file {numbers_path} does not exist.")
    else:
        # Read the numbers from file
        numbers = []
        with open(numbers_path, 'r') as file:
            for num in file.readlines():
                numbers.append(num.strip())

        print(numbers)

        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        link = 'https://web.whatsapp.com/'
        driver.get(link)

        # Wait for WhatsApp Web to load and for the user to scan the QR code
        time.sleep(30)

        # Send the message to each number in the list
        for number in numbers:
            link2 = f'https://web.whatsapp.com/send?phone=91{number}&text={msg}'
            driver.get(link2)
            time.sleep(20)
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER).perform()

            time.sleep(10)

        # Optionally close the browser after sending messages
        driver.quit()
