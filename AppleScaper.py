class Scraper:
    from platform import system
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    def __init__(self, country_code: str = "us"):
        self.apple_store_link = ""
        self.country_code = ""
        self.driver = None
        self.system = ""
        self.supported_country_codes = ("us", "uk")
        self.supported_systems = "Windows"

        self.set_system()
        self.set_country_code(country_code)
        self.set_driver()

    def set_country_code(self, country_code):
        self.country_code = str(country_code).lower()

    def get_country_code(self):
        return self.country_code

    def set_driver(
        self,
        path_to_driver: str = r"webdriver/chromedriver.exe",
    ):
        service = self.Service(path_to_driver)
        # remove options when done
        options = self.Options()
        options.add_experimental_option("detach", True)

        self.driver = self.webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        return self.driver

    def get_driver(self):
        return self.driver

    def set_system(self, system: str = system()):
        if system in self.supported_systems:
            self.system = system

    def get_system(self):
        return self.system


if __name__ == "__main__":
    scraper = Scraper("uk")
