from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Path to your Chrome webdriver. Download from https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_driver_path = "C:\webdrivers\chromedriver.exe"

# Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new instance of the Chrome driver with incognito mode
chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# List to store unique links
unique_links = set()

def save_links_to_file(links):
    with open("new_tabs_links.txt", "w") as file:
        for link in links:
            file.write(link + "\n")

try:
    # Open Chrome in incognito mode
    driver.maximize_window()
    driver.get("https://www.google.com")

    # Example: Perform a search
    search_box = driver.find_element("name", "q")
    search_box.send_keys("example search")
    search_box.send_keys(Keys.RETURN)

    # Wait for some time for the search results to load
    time.sleep(5)

    # Get all opened tabs
    tab_handles = driver.window_handles

    # Switch to each tab and get its URL
    for handle in tab_handles:
        driver.switch_to.window(handle)
        url = driver.current_url
        if url not in unique_links:
            unique_links.add(url)

    # Save the unique links to a file
    save_links_to_file(unique_links)

    print("Links saved to 'new_tabs_links.txt'")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser
    driver.quit()
