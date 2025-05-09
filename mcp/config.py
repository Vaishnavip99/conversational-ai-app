import os
from dotenv import load_dotenv

load_dotenv()

def get_default_model():
    return os.getenv("ACTIVE_MODEL", "gpt-3.5-turbo")
