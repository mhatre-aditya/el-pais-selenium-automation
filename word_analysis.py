from collections import Counter
import re


def analyze_titles(articles):

    words = []

    for article in articles:
        title = article["title_en"].lower()

        split_words = re.findall(r'\b\w+\b', title)

        words.extend(split_words)

    freq = Counter(words)

    print("\nWord Frequency (>2):\n")

    for word, count in freq.items():
        if count > 2:
            print(word, ":", count)