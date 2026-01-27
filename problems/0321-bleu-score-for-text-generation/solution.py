import numpy as np
from collections import Counter
import math

def get_ngrams(tokens, n):
    # ngrams = []
    # for i in range(len(tokens) - n + 1):
    #     fragment = tokens[i: i + n]
    #     ngrams.append(tuple(fragment))
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def bleu_score(candidate: list[str], references: list[list[str]], max_n: int = 4) -> float:
    """
    Calculate BLEU score for a candidate sentence against reference sentences.
    
    Args:
        candidate: List of tokens in the candidate sentence
        references: List of reference sentences, each as a list of tokens
        max_n: Maximum n-gram order (default: 4)
    
    Returns:
        BLEU score between 0 and 1
    """
    # Your code here
    if not candidate:
        return 0.0
    c_len = len(candidate)
    ref_lengths = [len(r) for r in references]
    r_len = min(ref_lengths, key=lambda x:(abs(x - c_len), x))
    precisions = []
    for n in range(1, max_n + 1):
       