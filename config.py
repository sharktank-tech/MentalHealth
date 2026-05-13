import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # ===============================
    # Flask
    # ===============================
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret")