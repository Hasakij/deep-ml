def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    order_map = {val: i for i,val in enumerate(order)}
    res = []
    for v in values:
        if v not in order_map:
            res.append(-1)
        else:
            res.append(order_map[v])
    return res
