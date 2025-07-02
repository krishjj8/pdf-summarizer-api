from transformers import pipeline
from langdetect import detect
from googletrans import Translator

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator = Translator()

def detect_and_translate(text):
    try:
        lang = detect(text)
        if lang != "en":
            translated = translator.translate(text, src=lang, dest="en").text
            return translated, lang
        return text, "en"
    except:
        return text, "unknown"

def summarize_text(text, mode="medium"):
    text, original_lang = detect_and_translate(text)
    if not text.strip():
        return "Input text is empty or invalid."

    if mode == "short":
        chunk_size, max_len = 600, 60
    elif mode == "detailed":
        c
