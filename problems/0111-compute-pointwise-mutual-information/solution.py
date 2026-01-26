import numpy as np

def compute_pmi(joint_counts, total_counts_x, total_counts_y, total_samples):
	# Implement PMI calculation here
	p_xy = joint_counts / total_samples
	p_x = total_counts_x / total_samples
	p_y = total_counts_y / total_samples
	pmi = np.log2(p_xy / (p_x * p_y))
	return round(float(pmi),3)