from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_embeddings(chunks: list[dict]) -> list[dict]:
    texts = [chunk["text"] for chunk in chunks]

    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )

    for i, chunk in enumerate(chunks):
        chunk["embedding"] = response.data[i].embedding

    return chunks

def embed_query(question: str) -> list[float]:
    response = client.embeddings.create(
        input=[question],
        model="text-embedding-3-small"
    )
    return response.data[0].embedding