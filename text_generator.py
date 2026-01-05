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
    Summary:
        Generate text using a specified LLM model, with optional self-consistency
        sampling for more reliable outputs. The generated result is printed in
        a formatted manner for easier debugging and readability.

    Args:
        client: LLM client instance that exposes a `models.generate_content(...)` method.
        model_name (str): Model identifier/name to use for text generation.
        system_prompt (str): System-level prompt or context provided to the model.
        user_prompt (str): User query or instruction passed to the model.
        config (Optional[dict]): Optional generation configuration (e.g., temperature,
            max tokens, top_p).
        use_self_consistency (bool): If True, generate multiple outputs and return
            a consensus result using self-consistency voting. If False, perform
            a single-pass generation.

    Return:
        str: The generated text output, either from self-consistency consensus
        or a single generation pass. Returns an error message if generation fails.
    """

    if use_self_consistency:
        # Use multiple generation paths and majority voting for improved reliability
        output = self_consistent_generate(
            client=client,
            model_name=model_name,
            contents=[user_prompt],
            config=config
        )
    else:
        try:
            # Single-pass generation without self-consistency
            response = client.models.generate_content(
                model=model_name,
                contents=[user_prompt],
                config=config
            )
            output = response.text if response and response.text else "No response"
        except Exception as e:
            output = f"Single pass failed: {str(e)}"

    # Print formatted prompts and output for debugging/traceability
    print_output(system_prompt, user_prompt, output)
    return output
