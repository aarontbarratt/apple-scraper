# AppleScraper

AppleScraper checks the Apple Certified Refurbished page for new devices added to the site. Whenever it finds devices
it will create a desktop notification and output the URLs to `output.txt`.

## Usage

```python3
import AppleHtmlParser

apple_scraper = AppleScraper("mac", "macbook-air", "uk")
apple_scraper.go()
```

Then create a `bash` file to run the `main.py` script on a schedule.

## License

[MIT](https://choosealicense.com/licenses/mit/)
