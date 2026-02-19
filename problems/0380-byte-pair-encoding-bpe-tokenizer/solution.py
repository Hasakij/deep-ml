from collections import Counter
def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """
    current_corpus = {tuple(k.split()): v for k, v in corpus.items()} # single char 'h' 'u' 'g'
    all_merges = []
    for _ in range(num_merges):
        # counting pairs
        pairs = Counter()
        for word, freq in current_corpus.items():
            for i in range(len(word) - 1):
                pair = (word[i], word[i+1])
                pairs[pair] += freq
        if not pairs:
            break

        # choosing the best pair
        best_pair = max(pairs