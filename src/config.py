# Generic config
RANDOM_SEED = 42
DATA_SUBSET = 1.0
VAL_SPLIT = 0.2
UNK_TOKEN = "[UNK]"
PAD_TOKEN = "[PAD]"

# Recurrent-based models config
EMBEDDING_DIMENSION = 25
EMBEDDING_MODEL_NAME = "glove-twitter-25"
MAX_CONTEXT_TOKENS = 100

# Transformer-based models config
MAX_BERT_TOKENS = 512
BERT_VOCAB_PATH = "data/bert-base-uncased-vocab.txt"
