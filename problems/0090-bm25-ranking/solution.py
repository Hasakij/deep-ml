import numpy as np
import math
from collections import Counter

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
	# Your code here
	if not corpus:
		return []
	N = len(corpus)
	total_length = sum(len(doc) for doc in corpus)
	avg_doc_len = total_length / N
	
	# IDF for every word in query 
	idf_values = {}
	for q_word in query:
		df_t = sum(1 for doc in corpus if q_word in doc)
		idf = math.log((N + 1) / ((df_t) + 1))
		idf_values[q_word] = idf
	
	# BM25 scores
	all_doc_scores = []
	for document in corpus:
		doc_len = len(document)
		total_score = 0
		for q_word in query:
			f = document.count(q_word)

			if f > 0:
				numerator = f * (k1 + 1)
				denominator = f + k1 * (1 - b + b *(doc_len / avg_doc_len))
				word_score = idf_values[q_word] * numerator / denominator
				total_score += word_score
		all_doc_scores.append(total_score)

	return np.round(all_doc_scores,3)