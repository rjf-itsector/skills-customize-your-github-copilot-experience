from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI app instance
app = FastAPI(title="Student API", description="A simple REST API built with FastAPI")

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None

# In-memory storage (replace with database in production)
items = []

# TODO: Implement your API endpoints here

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to your FastAPI application!"}

# TODO: Add CRUD endpoints:
# GET /items - Get all items
# GET /items/{item_id} - Get single item
# POST /items - Create new item
# PUT /items/{item_id} - Update item
# DELETE /items/{item_id} - Delete item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)