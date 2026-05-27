import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    #
    # ==== Flask =====
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret")

    # ==== Caminho das pastas =====
    FLASHCARDS = os.getenv("FLASK_FLASHCARDS", "True")
    WORD_LISTS = os.path.join(os.getcwd(), "word_lists")
    TYPING_TEXTS =  os.path.join(os.getcwd(), "typing_texts")