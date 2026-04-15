import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.embeddings import embed_query

def test_embed_query():
    question = "What is the project planning process?"
    vector = embed_query(question)

    print(f"Vector dimensions: {len(vector)}")
    print(f"First 5 values: {vector[:5]}")

    assert len(vector) == 1536
    assert isinstance(vector[0], float)
    print("embed_query passed")

if __name__ == "__main__":
    test_embed_query()