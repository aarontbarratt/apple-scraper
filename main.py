from html.parser import HTMLParser


class AppleScraper(HTMLParser):
    def __init__(self, device, model, region):
        super().__init__()
        import requests
        from plyer import notification

        self.html = ""
        self.notification = notification
        self.products = []
        self.requests = requests
        self.url = ""
        self.requirements = {}

        self.set_requirements(device, model, region)
        self.set_url()
        self.set_html()

    def go(
        self,
    ):
        self.feed(self.get_html())
        if len(self.products) > 0:
            self.notify()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if (
            tag == "a"
            and "shop/product" in attrs[0][1]
            and self.requirements["model"] in attrs[0][1]
        ):
            attribute = attrs[0][1]
            self.products.append(f"https://www.apple.com{attribute}")

    def notify(self):
        self.notification.notify(
            title=f"{self.requirements['model']} found!",
            message="Check logs now",
            app_name="Apple Peeler",
        )
        # TODO: put the apple store top level link at the start of the file
        # TODO: make the output writer a separate function
        with open("output.txt", "w") as file:
            for product in self.products:
                file.write(f"{product}\n")

    def set_html(self):
        response = self.requests.get(self.get_url())
        if response.url != self.get_url():
            print(f"Not matched. Requested: {self.get_url()}, response: {response.url}")
        else:
            self.html = response.text

    def get_html(self) -> str:
        return self.html

    def set_products(self):
        pass

    def get_products(self) -> list[str]:
        return self.products

    def set_requirements(self, device: str, model: str, region: str) -> None:
        """
        Set the requirements for the products you want to track.
        :param device: device type e.g. mac/ipad/iphone
        :param model: model of the device. example: macbook-air/mac-mini
        :param region: the country code of the Apple website you wish to purchase from
        :return: None
        """
        self.requirements = {"device": device, "model": model, "region": region}
        self.set_url()
        self.set_html()

    def get_requirements(self) -> dict[str, str]:
        """
        gets the currently set requirements
        :return: dict[str, str, str]
        """
        return self.requirements

    def set_url(self):
        self.url = (
            f"https://www.apple.com/{self.requirements['region']}/shop/refurbished/{self.requirements['device']}/"
            f"{self.requirements['model']}"
        )

    def get_url(self):
        return self.url


if __name__ == "__main__":
    ac = AppleScraper("mac", "macbook-air", "uk")
    ac.go()
