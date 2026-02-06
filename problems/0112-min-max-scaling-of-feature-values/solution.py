def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    max_num = max(x)
    min_num = min(x)
    res = []
    for n in x:
        num = (n - min_num) / (max_num - min_num) 
        res.append(num)
    return res