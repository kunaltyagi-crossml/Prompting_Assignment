"""
utils.py
--------
Helper utilities used across the project.
"""

import time
import re
from collections import Counter
from typing import Optional


def print_output(system_prompt, user_prompt, output):
    print("\n" + "-" * 60)
    print("PROMPT:")
    print(system_prompt, "\n", user_prompt)
    print("\nOUTPUT:")
    print(output)
    print("-" * 60)


def retry_delay(seconds=2):
    time.sleep(seconds)


def extract_final_answer(text: str) -> str:
    patterns = [
        r'(?:total|final|answer|result|amount)[:\s]*\$?([0-9,]+\.?[0-9]*)',
        r'\$([0-9,]+\.?[0-9]*)'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).replace(",", "").strip()
    return "No answer extracted"


def self_consistent_generate(
    client,
    model_name: str,
    contents: list,
    config: Optional[dict] = None,
    n_samples: int = 5
) -> str:
    answers = []

    for i in range(n_samples):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=config
            )
            if response and response.text:
                ans = extract_final_answer(response.text)
                answers.append(ans)
                print(f"Path {i+1}: {ans}")
            else:
                answers.append("Empty")
        except Exception:
            answers.append("Error")
            retry_delay()

    valid = [a for a in answers if a not in ("Error", "Empty", "No answer extracted")]

    if valid:
        consensus = Counter(valid).most_common(1)[0][0]
        return f"Consensus: {consensus}\nVotes: {dict(Counter(valid))}"

    return f"No consensus (raw: {dict(Counter(answers))})"
