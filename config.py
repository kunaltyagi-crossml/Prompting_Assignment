"""
config.py
---------
Centralized configuration for model selection,
system instructions, and generation parameters.
"""

from google.genai import types
from prompts import system_prompt

# Model configuration
MODEL_NAME = "gemini-2.5-flash"

# Generation configuration
CONFIG = types.GenerateContentConfig(
    system_instruction=system_prompt,
    temperature=0.2,
    top_p=0.5,
    top_k=10,
    max_output_tokens=5000
)
