from fastapi import FastAPI
from app.routers import ask, sync

app = FastAPI(title="Doc SummAIriser API")

app.include_router(ask.router)
app.include_router(sync.router)

@app.get("/")
def health_check():
    return {"status": "ok"}