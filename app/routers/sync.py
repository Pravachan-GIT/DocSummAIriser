# from fastapi import APIRouter

# router = APIRouter()

# @router.post("/sync")
# def sync(tenant_id: str):
#     return {"status": "ok", "message": f"Sync triggered for tenant: {tenant_id}"}

from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from app.services.confluence_connector import get_all_pages
from app.services.chunker import chunk_text
from app.services.embeddings import generate_embeddings
from app.services.vector_store import upsert_chunks

router = APIRouter()

class SyncRequest(BaseModel):
    org_id: str
    space_key: str

def run_sync(org_id: str, space_key: str):
    print(f"[sync] Starting sync for org={org_id} space={space_key}")

    # Step 1 — pull pages from Confluence (already returns clean text)
    pages = get_all_pages(space_key)
    print(f"[sync] Fetched {len(pages)} pages")

    all_chunks = []

    # Step 2 — chunk each page (no clean_html needed, connector already strips HTML)
    for page in pages:
        chunks = chunk_text(
            text=page["text"],
            page_id=page["page_id"],
            page_title=page["title"],
            space_key=page["space_key"]
        )
        all_chunks.extend(chunks)

    print(f"[sync] Total chunks: {len(all_chunks)}")

    # Step 3 — generate embeddings
    chunks_with_embeddings = generate_embeddings(all_chunks)

    # Step 4 — store in Pinecone
    count = upsert_chunks(chunks_with_embeddings, org_id=org_id)
    print(f"[sync] Upserted {count} vectors for org={org_id}")

@router.post("/sync")
async def sync(request: SyncRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        run_sync,
        org_id=request.org_id,
        space_key=request.space_key
    )
    return {"status": "sync started", "org_id": request.org_id, "space_key": request.space_key}