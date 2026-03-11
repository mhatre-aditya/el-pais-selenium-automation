El País Opinion Scraper Automation

This project automates scraping articles from the El País Opinion section using Selenium.

Features

- Opens the El País Opinion page
- Scrapes the first 5 opinion articles
- Extracts Spanish titles and main article content
- Downloads cover images
- Translates titles from Spanish to English
- Performs word frequency analysis on translated titles
- Runs parallel tests across multiple browsers/devices using BrowserStack

Technologies Used

- Python
- Selenium
- BeautifulSoup
- Deep Translator API
- BrowserStack
- GitHub

Project Structure

project/
│
├── main.py
├── scraper.py
├── translator.py
├── word_analysis.py
├── browserstack_config.py
├── requirements.txt
└── README.md

Running Locally

1. Clone the repository

git clone <https://github.com/mhatre-aditya/el-pais-selenium-automation>

2. Install dependencies

pip install -r requirements.txt

3. Run the script

python main.py

BrowserStack Testing

The automation runs in parallel on:

- Chrome (Windows 11)
- Firefox (Windows 11)
- Edge (Windows 11)
- Chrome (MacOS)
- Safari (iPhone 14)

BrowserStack Build Link:

<https://automate.browserstack.com/projects/ElPais+Automation/builds/Parallel+Test/1?public_token=3bdd5406bb1f57b14c182867cf02a872dd3565618d49643331b73db2fc500915>

Output

- Spanish article titles
- English translated titles
- Word frequency analysis