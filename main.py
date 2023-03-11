from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from uuid import uuid1
from time import sleep


options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

requirements = {"device": "mac", "model": "macbook-air"}

region = "uk"

built_url = f"https://www.apple.com/{region}/shop/refurbished/{requirements['device']}/{requirements['model']}"
driver.get(built_url)

if driver.current_url != built_url:
    driver.quit()
elif driver.current_url == built_url:
    sleep(2)
    driver.save_screenshot(rf"images\{uuid1()}.png")
    driver.quit()
