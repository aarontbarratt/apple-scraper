# AppleScraper

AppleScraper periodically checks the Apple Certified Refurbished page for new devices added to the site.

## Installation

1. Clone this repo to your preferred location
2. Navigate to your newly created repo
3. Run the following command

```bash
python3 main.py
```

## Usage

```python3
import AppleScraper

# returns 'words'
AppleScraper.set_devices('iPad', 'mac_mini', 'iMac')

# returns dictionary of available devices
AppleScraper.Run()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)