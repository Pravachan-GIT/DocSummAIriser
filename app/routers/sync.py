from fastapi import APIRouter

router = APIRouter()

@router.post("/sync")
def sync(tenant_id: str):
    return {"status": "ok", "message": f"Sync triggered for tenant: {tenant_id}"}