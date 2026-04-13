import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.embeddings import generate_embeddings
from app.services.vector_store import upsert_chunks, index

def test_upsert_chunks():
    sample_chunks = [
        {
            "text": "This is a test Confluence page about project planning.",
            "page_id": "TEST-PAGE-001",
            "page_title": "Project Planning",
            "space_key": "TEST"
        }
    ]

    # generate real embeddings first
    chunks_with_embeddings = generate_embeddings(sample_chunks)

    # upsert into Pinecone
    count = upsert_chunks(chunks_with_embeddings, org_id="test_org")
    print(f"Upserted {count} vectors")

    # verify it landed in Pinecone
    stats = index.describe_index_stats()
    total = stats["total_vector_count"]
    print(f"Total vectors in index: {total}")

    assert count == 1
    assert total >= 1
    print("upsert_chunks passed")

if __name__ == "__main__":
    test_upsert_chunks()