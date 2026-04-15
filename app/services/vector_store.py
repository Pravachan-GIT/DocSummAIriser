from pinecone import Pinecone
import os

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

def upsert_chunks(chunks: list[dict], org_id: str) -> int:
    vectors = []

    for chunk in chunks:
        vector_id = f"{org_id}_{chunk['page_id']}_{chunks.index(chunk)}"

        vectors.append({
            "id": vector_id,
            "values": chunk["embedding"],
            "metadata": {
                "text": chunk["text"],
                "page_id": chunk["page_id"],
                "page_title": chunk["page_title"],
                "space_key": chunk["space_key"],
                "org_id": org_id
            }
        })

    index.upsert(vectors=vectors)
    return len(vectors)

def search_chunks(query_vector: list[float], org_id: str, top_k: int = 5) -> list[dict]:
    results = index.query(
        vector=query_vector,
        top_k=top_k,
        filter={"org_id": {"$eq": org_id}},
        include_metadata=True
    )

    chunks = []
    for match in results["matches"]:
        chunks.append({
            "text": match["metadata"]["text"],
            "page_id": match["metadata"]["page_id"],
            "page_title": match["metadata"]["page_title"],
            "space_key": match["metadata"]["space_key"],
            "score": round(match["score"], 4)
        })

    return chunks