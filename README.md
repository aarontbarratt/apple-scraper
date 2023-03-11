# AppleScraper

AppleScraper checks the Apple Certified Refurbished page for new devices added to the site. Whenever it finds devices
it will create a desktop notification and output the URLs to `output.txt`.

## Usage

```python3
import AppleHtmlParser

apple_scraper = AppleScraper("mac", "macbook-air", "uk")
apple_scraper.go()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
