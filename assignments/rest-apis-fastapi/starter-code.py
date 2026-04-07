from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="My Items API")

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., max_length=200)

# In-memory data store
items: dict[int, Item] = {}

# ---------------------------------------------------------------------------
# Task 1 — Root endpoint
# ---------------------------------------------------------------------------

@app.get("/")
def read_root():
    # TODO: return a JSON welcome message
    pass

# ---------------------------------------------------------------------------
# Task 2 — CRUD endpoints
# ---------------------------------------------------------------------------

@app.get("/items")
def list_items(search: Optional[str] = None, skip: int = 0, limit: int = 10):
    # TODO: return all items, with optional search/pagination (Task 3)
    pass

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: return the item with the given ID, or raise a 404 error
    pass

@app.post("/items", status_code=201)
def create_item(item: Item):
    # TODO: add the item to the store and return it
    pass

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: update the item with the given ID, or raise a 404 error
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: delete the item with the given ID, or raise a 404 error
    pass

# ---------------------------------------------------------------------------
# Run with: uvicorn starter-code:app --reload
# ---------------------------------------------------------------------------
