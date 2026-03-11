from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

from scraper import scrape_articles
from translator import translate_titles
from word_analysis import analyze_titles
from browserstack_config import BROWSERSTACK_URL, browsers


def run_test(cap):

    try:

        print("Starting test:", cap)

        options = Options()

        for key, value in cap.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options
        )

        articles = scrape_articles(driver)
        articles = translate_titles(articles)

        for article in articles:
            print("Spanish:", article["title_es"])
            print("English:", article["title_en"])

        analyze_titles(articles)

        driver.quit()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_test, browsers)