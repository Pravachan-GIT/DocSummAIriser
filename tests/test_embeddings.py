import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.embeddings import generate_embeddings

def test_generate_embeddings():
    sample_chunks = [
        {
            "text": "Confluence is a team collaboration tool.",
            "page_id": "PAGE-001",
            "page_title": "Test Page",
            "space_key": "TEST"
        },
        {
            "text": "It allows teams to create and share documentation.",
            "page_id": "PAGE-001",
            "page_title": "Test Page",
            "space_key": "TEST"
        }
    ]

    result = generate_embeddings(sample_chunks)
    # print("*"*50)
    print(f"Number of chunks embedded: {len(result)}")
    print(f"Embedding dimensions: {len(result[0]['embedding'])}")
    print(f"First 5 values: {result[0]['embedding'][:5]}")

    assert len(result) == 2
    assert "embedding" in result[0]
    assert len(result[0]["embedding"]) == 1536
    print("generate_embeddings passed")

if __name__ == "__main__":
    test_generate_embeddings()