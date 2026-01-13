import string

def normalize_text(text: str) -> str:
    text = text.lower()
    table = str.maketrans("", "", string.punctuation)
    text = text.translate(table)
    text = "".join(text.split())
    return text
def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    # Your code here
    if not predictions or not references:
        return 0.0
    matches = 0
    for p, r in zip(predictions, references):
        if normalize_text(p) == normalize_text(r):
            matches += 1
        
    return matches / len(predictions)
