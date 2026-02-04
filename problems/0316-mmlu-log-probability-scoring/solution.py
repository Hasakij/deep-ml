import numpy as np

def mmlu_log_prob_score(log_probs: list, correct_answers: list) -> dict:
    """
    Compute MMLU-style log-probability scoring metrics.
    
    Args:
        log_probs: List of lists, where each inner list contains 
                   log-probabilities for each answer choice
        correct_answers: List of correct answer indices (0-indexed)
    
    Returns:
        Dictionary with 'accuracy', 'predictions', and 'avg_correct_prob'
    """
    log_probs_arr = np.array(log_probs)
    correct_idx_arr = np.array(correct_answers)
    predictions = np.argmax(log_probs_arr, axis=1)
    accuracy = np.mean(predictions == correct_idx_arr)
    row_max = np.max(log_probs_arr, axis=1, keepdims=True)
    shifted_exp = np.exp(log_probs_arr - row_max)
    probs_matrix = shifted_exp / np.sum(shifted_exp, axis=1, keepdims=True)
    row_indices = np.arange(len(correct_answers))
    correct_probs = probs_matrix[row_indices, correct_idx_arr]
    avg_correct_prob = np.mean(correct_pro