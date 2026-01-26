import numpy as np
from collections import Counter

def meteor_score(reference, candidate, alpha=0.9, beta=3, gamma=0.5):
    """
    Calculate METEOR score for machine translation evaluation.
    
    Args:
        reference: Reference translation string
        candidate: Candidate translation string
        alpha: Weight for precision vs recall in F-mean (default 0.9)
        beta: Exponent for fragmentation penalty (default 3)
        gamma: Maximum penalty coefficient (default 0.5)
    
    Returns:
        METEOR score between 0 and 1
    """
    # Your code here
    ref_tokens = reference.lower().split()
    cand_tokens = candidate.lower().split()
    ref_counts = Counter(ref_tokens)
    cand_counts = Counter(cand_tokens)
    matches_counts = ref_counts & cand_counts
    total_matches = sum(matches_counts.values())
    if total_matches == 0:
        return 0.0
    precision = total_matches / len(cand_tokens)
    recall = total_matches / len(ref_tokens)
    f_mean = (precision * 