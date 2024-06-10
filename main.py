import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

print("GitHub Views Farm")

while True:
    username = input("Enter your GitHub username: ")
    if username == ' ' or len(username) == 0:
        print("Please enter a GitHub username.")
    elif re.match(r'^[A-Za-z0-9-_]+$', username):
        print("Please enter a valid GitHub username.")
    else:
        break

def start_farm(target):
    url = f'https://github.com/{target}'
    chrome_options = Options()
  
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-service-autorun")
    chrome_options.add_argument("--password-store=basic")
    chrome_options.add_argument("--no-default-browser-check")
  
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get(url)
    print(f"Opened {url}")

    while True:
        time.sleep(2)
        driver.refresh()
        print(f"Refreshed {url} after 2 seconds")

if __name__ == "__main__":
    start_farm(target=username)
