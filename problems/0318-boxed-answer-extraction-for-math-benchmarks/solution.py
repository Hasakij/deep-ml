def extract_boxed_answer(response: str) -> str:
    """
    Extract the answer from within \boxed{...} in a model response.
    
    Args:
        response: The model's text response containing a boxed answer
    
    Returns:
        The content inside the last \boxed{}, or empty string if not found
    """
    # Your code here
    last_res = response.rfind(r"\boxed{")
    if last_res == -1:
        return ""
    start_index = last_res + 7
    res = ""
    depth = 1
    for i in range(start_index, len(response)):
        char = response[i]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        if depth == 0:
            return res
        res += char
    return ""