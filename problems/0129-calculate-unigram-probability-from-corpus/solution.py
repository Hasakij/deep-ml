def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    tokens = corpus.split()
    total_tokens = len(tokens)
    word_count = tokens.count(word)
    prob = word_count / total_tokens if total_tokens > 0 else 0
    return round(prob, 4)
