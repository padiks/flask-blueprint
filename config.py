import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "The quick brown fox jumps over the fence."
    # Add other global configs if needed
