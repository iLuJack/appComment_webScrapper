# Web Scraper for Google Play Store

## Overview
This project is a web scraper designed to fetch app reviews from the Google Play Store using the `google-play-scraper` library. The scraper retrieves reviews for specified app IDs and outputs them for analysis.

## Requirements
To run this project, you need to install the required Python packages. You can do this by using the `requirements.txt` file provided in the project.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/iLuJack/web_scrapper.git
   cd web_scrapper
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the scraper, execute the `play_store.py` script. You can specify the app IDs for which you want to fetch reviews.

### Example
```bash
python play_store.py
```

Make sure to replace the placeholder app IDs in the script with the actual app IDs you want to scrape.

## Output
The scraper will output the reviews to the console. You can modify the script to save the reviews to a file if needed.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [google-play-scraper](https://github.com/facundoolano/google-play-scraper) for providing the library to scrape Google Play Store data.