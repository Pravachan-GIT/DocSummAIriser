import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.embeddings import embed_query
from app.services.vector_store import search_chunks

def test_search_chunks():
    question = "Project planning"

    print(f"Embedding question...")
    query_vector = embed_query(question)

    print(f"Searching Pinecone...")
    results = search_chunks(query_vector, org_id="test_org", top_k=10)

    print(f"Found {len(results)} results")
    for i, chunk in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(f"Title:  {chunk['page_title']}")
        print(f"Score:  {chunk['score']}")
        print(f"Text:   {chunk['text'][:120]}...")

    assert len(results) >= 1
    assert "text" in results[0]
    assert "page_title" in results[0]
    assert "score" in results[0]
    print("\nsearch_chunks passed")

if __name__ == "__main__":
    test_search_chunks()