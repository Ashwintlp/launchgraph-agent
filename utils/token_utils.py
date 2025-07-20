import tiktoken

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

def chunk_text(text: str, max_tokens: int = 3000, model: str = "gpt-3.5-turbo") -> list[str]:
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [enc.decode(chunk) for chunk in chunks]

def chunk_text(text, max_length=3000):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]
