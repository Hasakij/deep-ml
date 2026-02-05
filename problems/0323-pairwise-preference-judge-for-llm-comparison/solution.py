def pairwise_preference_judge(comparisons: list, criteria_weights: dict, tie_threshold: float) -> dict:
    """
    Analyze pairwise comparisons between LLM responses.
    
    Args:
        comparisons: List of comparison dicts with 'id', 'scores_a', 'scores_b'
        criteria_weights: Dict mapping criterion names to importance weights
        tie_threshold: Maximum difference to declare a tie
    
    Returns:
        Dict with 'results', 'win_rate_a', 'win_rate_b', 'tie_rate', 'avg_margin'
    """
    # Your code here
    results_list = []
    if not comparisons:
        return {
            'results' : [],
            'win_rate_a': 0.0,
            'win_rate_b': 0.0,
            'tie_rate' : 0.0,
            'avg_margin' : 0.0
        }
    total_w = sum(criteria_weights.values())
    norm_weights = {k: v / total_w for k, v in criteria_weights.items()}
    count_a = count_b = count_tie = total_margin = 0
    for comp in comparisons:
        w_a = 0
        w_b = 0
        for crit