import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    denominator = 0
    result = []
    for score in scores:
        denominator += math.exp((score - max_score))
    for score in scores:
        res = math.exp((score - max_score)) / denominator
        result.append(res)
    return result