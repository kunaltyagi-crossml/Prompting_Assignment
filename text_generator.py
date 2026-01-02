from typing import Optional
from utils import print_output, self_consistent_generate


def generate_text(
    client,
    model_name: str,
    system_prompt: str,
    user_prompt: str,
    config: Optional[dict] = None,
    use_self_consistency: bool = True
) -> str:
    """
    Generates text using Gemini with optional self-consistency.
    """

    if use_self_consistency:
        output = self_consistent_generate(
            client=client,
            model_name=model_name,
            contents=[user_prompt],
            config=config
        )
    else:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=[user_prompt],
                config=config
            )
            output = response.text if response and response.text else "No response"
        except Exception as e:
            output = f"Single pass failed: {str(e)}"

    print_output(system_prompt, user_prompt, output)
    return output
