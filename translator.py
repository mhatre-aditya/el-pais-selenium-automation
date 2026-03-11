from deep_translator import GoogleTranslator

def translate_titles(articles):

    for article in articles:
        try:
            translated = GoogleTranslator(source='es', target='en').translate(article["title_es"])
            article["title_en"] = translated
        except Exception:
            article["title_en"] = "Translation failed"

    return articles