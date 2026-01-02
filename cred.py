"""
cred.py
--------
Loads and validates sensitive credentials (API keys).

Best Practices:
- Credentials are NOT hardcoded
- Values are loaded from environment variables
"""

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")
