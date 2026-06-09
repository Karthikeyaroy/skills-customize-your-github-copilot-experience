"""
FastAPI REST API Starter Code

This module provides a foundation for building a REST API with FastAPI.
Complete the TODO sections to implement full CRUD functionality.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Item API", version="1.0.0")

# ============================================================================
# Data Models
# ============================================================================

class Item(BaseModel):
    """Pydantic model for an item in inventory."""
    id: int
    name: str = Field(..., min_length=1, description="Item name")
    description: Optional[str] = Field(None, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be positive)")


# ============================================================================
# In-memory Data Store
# ============================================================================

# TODO: Initialize an empty list to store items
# items: List[Item] = []


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/items/", response_model=List[Item], tags=["Items"])
def list_items():
    """
    Retrieve all items from the store.
    
    Returns:
        List[Item]: A list of all items
    """
    # TODO: Return all items from the data store
    pass


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: Item):
    """
    Create a new item in the store.
    
    Args:
        item (Item): The item data
    
    Returns:
        Item: The created item with its ID
    """
    # TODO: Add the item to the data store and return it
    pass


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    """
    Retrieve a specific item by ID.
    
    Args:
        item_id (int): The ID of the item to retrieve
    
    Returns:
        Item: The requested item
    
    Raises:
        HTTPException: If the item is not found (404)
    """
    # TODO: Find and return the item with the given ID
    # TODO: Raise HTTPException with status_code=404 if not found
    pass


@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: int, updated_item: Item):
    """
    Update an existing item.
    
    Args:
        item_id (int): The ID of the item to update
        updated_item (Item): The updated item data
    
    Returns:
        Item: The updated item
    
    Raises:
        HTTPException: If the item is not found (404)
    """
    # TODO: Find the item with the given ID
    # TODO: Update its fields with the new data
    # TODO: Return the updated item
    # TODO: Raise HTTPException with status_code=404 if not found
    pass


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    """
    Delete an item from the store.
    
    Args:
        item_id (int): The ID of the item to delete
    
    Raises:
        HTTPException: If the item is not found (404)
    """
    # TODO: Find and remove the item with the given ID
    # TODO: Raise HTTPException with status_code=404 if not found
    pass


# ============================================================================
# Health Check Endpoint
# ============================================================================

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
