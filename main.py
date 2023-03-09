from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path_to_driver = r"webdriver/chromedriver.exe"
service = Service(path_to_driver)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

devices = {
    "mac": ("macbook-air", "macbook-pro", "imac", "mac-mini", )
}

country_code = "uk"
device = "mac"
model = "mac-mini"

driver.get(f"https://www.apple.com/us/shop/refurbished/mac/mac-mini-32gb")
