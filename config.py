from dataclasses import dataclass

@dataclass
class Config:
    batch_size : int = 32,
    max_features : int = 20000,
    embedding_dim : int = 128,
    sequence_length : int = 500,