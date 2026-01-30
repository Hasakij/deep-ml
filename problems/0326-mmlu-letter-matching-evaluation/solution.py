import re
def extract_letter(text):
    text = text.upper()
    match = re.search(r'\(([A-D])\)', text) # char in parentheses ()
    if match: return match.group(1)
    match = re.search(r'\b([A-D])[\.\)]', text) # char with . or () at start or end
    if match: return match.group(1)
    match = re.search(r'(?:ANSWER IS|CHOICE IS|IS[:\s]+)([A-D])\b', text) # phrase "is A" "is: A"
    if match: return match.group(1)
    match = re.search(r'\b([A-D])\b', text) # separate char (constrained with words bounds \b)
    if match: return match.group(1)
    return None
def mmlu_letter_matching(model_outputs: list[str], ground_truth: list[str], subjects: list[str]) -> dict:
    """
    Evaluate MMLU predictions using letter-matching.
    
    Args:
        model_outputs: List of model generated responses
        ground_truth: List of correct answer letters (A, B, C, or D)
        subjects: List of subject names for each question
    
    Returns:
        Dictionary with evaluation metrics
    """