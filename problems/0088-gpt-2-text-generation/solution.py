import numpy as np
def gen_text(prompt: str, n_tokens_to_generate: int = 40):
	encoder, hparams, params = load_encoder_hparams_and_params()
	tokens = encoder.encode(prompt) # hello -> [1]
	generated_tokens = []
	for _ in range(n_tokens_to_generate):
		logits = gpt2_simple(tokens, params, hparams)
		last_token_logits = logits[-1]
		next_token = int(np.argmax(last_token_logits))
		tokens.append(next_token)
		generated_tokens.append(next_token)
	return encoder.decode(generated_tokens)

def gpt2_simple(tokens, params, hparams):
	x = params["wte"][tokens]
	x += params["wpe"][:len(tokens)]
	x = layer_norm(x, **params["ln_f"])
	logits = x @ params["wte"].T
	return logits
def layer_norm(x, g, b, eps=1e-5):
	mean = np.mean(x, axis=-1, keepdims=True)
	variance = np.var(x, axis=-1, keepdims=True)
	return g * (x - mean) / np.sqrt(variance + eps) + b

def load_encoder_hparams_and_params(model_size: str = "124M", models_dir: str = "models"):
	class DummyBPE:
		def __init__(self):
			self.encoder_dic