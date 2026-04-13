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