import numpy as np
import math
def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	if not corpus:
		return []
	N = len(corpus)
	# IDF
	idf_values = {}
	for q_word in query:
		df_t = sum(1 for doc in corpus if q_word in doc)
		idf = math.log((N + 1) / (df_t + 1)) + 1
		idf_values[q_word] = idf
	
	# TF-IDF
	output = []
	for document in corpus:
		scores_for_this_doc = []
		doc_len = len(document)
		for q_word in query:
			if doc_len == 0:
				tf = 0
			else:
				tf = document.count(q_word)/ doc_len
			score = tf * idf_values[q_word]
			scores_for_this_doc.append(round(score, 5))
		output.append(scores_for_this_doc)
	return output



