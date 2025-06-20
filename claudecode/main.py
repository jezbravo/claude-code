from fastapi import FastAPI

app = FastAPI(
    title="Claude Code API",
    description="A FastAPI application for Claude Code",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World", "app": "Claude Code API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}