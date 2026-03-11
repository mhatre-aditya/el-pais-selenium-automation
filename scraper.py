import os
import requests
from bs4 import BeautifulSoup


def scrape_articles(driver):

    driver.get("https://elpais.com/opinion/")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    articles = []

    article_tags = soup.select("article h2 a")

    links = []
    titles = []

    for tag in article_tags:
        title = tag.get_text(strip=True)
        link = tag.get("href")

        if title and link:
            titles.append(title)
            links.append(link)

        if len(titles) == 5:
            break

    for i, link in enumerate(links):

        driver.get(link)

        article_soup = BeautifulSoup(driver.page_source, "html.parser")

        paragraphs = article_soup.select("p")

        content = " ".join(
            [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
        )

        image_url = None

        img = article_soup.select_one("figure img")

        if img:
            image_url = img.get("src")

            os.makedirs("images", exist_ok=True)

            try:
                img_data = requests.get(image_url).content
                with open(f"images/article_{i}.jpg", "wb") as f:
                    f.write(img_data)
            except:
                pass

        articles.append({
            "title_es": titles[i],
            "content": content,
            "image": image_url
        })

    return articles