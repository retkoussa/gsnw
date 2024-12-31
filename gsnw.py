'''
    This script currentlt "JUST WORKS"
    Nothing fancy yet.
    Enjoy :)
'''
import time
import logging
import os
import argparse
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import chromedriver_autoinstaller

# Banner
banner = '''
---------------------------------
GSNW                                                                                                             
Find me on X (Twitter) @retkoussa 
---------------------------------
'''

# Install the Chrome driver automatically
chromedriver_autoinstaller.install()

# Disable logging for Selenium and other verbose outputs
seleniumLogger.setLevel(logging.WARNING)
logging.getLogger('WDM').setLevel(logging.NOTSET)
logging.getLogger('urllib3').setLevel(logging.WARNING)

# Suppress DevTools listening message
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")

def search_github(query):
    matched_words = set()  # Use a set to store unique matched words
    page_number = 1
    base_url = f"https://github.com/search?q=path%3A%2F{query}&type=code&p="

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--profile-directory=Default")
    
    # Current user
    current_user = os.getlogin()
    
    # IMPORTANT
    # Make sure you're logged in to Github on the specificed Chrome Profile
    chrome_options.add_argument(f"--user-data-dir=C:\\Users\\{current_user}\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    while True:
        # Construct the URL for the current page
        url = f"{base_url}{page_number}"
        driver.get(url)

        try:
            # Wait until the elements are located or timeout after 10 seconds
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "prc-Link-Link-85e08"))
            )

            if elements:
                for element in elements:
                    try:
                        path = element.text
                        segments = path.split('/')
                        for segment in segments:
                            if query.lower() in segment.lower() and segment not in matched_words:
                                print(f"\t[x] {segment}")
                                matched_words.add(segment)

                    except StaleElementReferenceException:
                        print("Encountered a stale element, continuing...")
            else:
                print(f"Error: No elements found on page {page_number}")
                break

            # Check if there are no results for the next page
            no_results_message = driver.find_elements(By.XPATH, "//h3[contains(text(), 'Your search did not match any')]")
            if no_results_message:
                break

            # Increment the page number for the next iteration
            page_number += 1
            time.sleep(2)  # Add a short delay to avoid making requests too quickly
        except Exception as e:
            print(f"Error: {e}")
            break

    driver.quit()
    return list(matched_words)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_query", help="The search query to use for GitHub code search")
    parser.add_argument("output_file", nargs='?', default=None, help="The output file to save the results")
    parser.add_argument("-silent", action="store_true", help="Suppress the banner")

    args = parser.parse_args()
    search_query = args.search_query
    output_file = args.output_file

    if not args.silent:
        print(banner)

    matched_words = search_github(search_query)

    if output_file:
        with open(output_file, "w") as file:
            for word in matched_words:
                file.write(word + "\n")
    
    # Yeah im aware its bad execution D:

    else:
        print('-------------------------')
        for word in matched_words:
            print(word)
        print('-------------------------')


if __name__ == "__main__":
    main()
