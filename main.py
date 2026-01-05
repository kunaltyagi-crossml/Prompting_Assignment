"""
main.py
-------
Application entry point for the LLM text generation project.
"""

from client import client
from config import CONFIG, MODEL_NAME
from prompts import system_prompt, user_prompt
from text_generator import generate_text


def main():
    """
    Summary:
        Calls the text generation function with the configured client,
        model name, system prompt, user prompt, and generation settings.

    Args:
        None

    Returns:
        None
    """
    generate_text(
        client=client,
        model_name=MODEL_NAME,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        config=CONFIG,
        use_self_consistency=True
    )


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
