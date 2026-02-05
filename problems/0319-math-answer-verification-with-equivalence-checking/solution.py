import re
import math

def parse_to_float(text: str) -> float:
    try:
        text = text.lower().replace(" ", "")
        text = text.replace("sqrt", "math.sqrt")
        text = text.replace("pi", "math.pi")
        return float(eval(text, {"math": math, "__builtins__": {}}))
    except:
        return float('nan')
    # while "sqrt(" in text:
    #     start = text.find("sqrt(")
    #     end = text.find(")", start)
    #     inside = text[start + 5:end]
    #     val =  math.sqrt(float(inside))
    #     text = text[:start] + str(val) + text[end + 1:]
    # if "/" in text:
    #     parts = text.split("/")
    #     return float(parts[0]) / float(parts[1])
    # return float(text)

def verify_math_answer(predicted: str, ground_truth: str, tolerance: float = 1e-6) -> bool:
    """
    Verify if two mathematical answers are equivalent.
    
    Args:
        predicted: The predicted answer string
        ground_truth: The ground truth answer string
        tolerance: Numerical toler