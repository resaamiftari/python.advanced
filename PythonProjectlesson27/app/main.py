
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

from app.database import get_db, init_db

# Leximi i variablave nga .env
load_dotenv()

# Krijimi i aplikacionit FastAPI
app = FastAPI(title="Items API")

# Inicializimi i databazës
init_db()

# Marrja e API Key nga header-i
api_key_header = APIKeyHeader(
    name="api-key",
    auto_error=False
)


# Kontrollimi i API Key
def check_key(key: Optional[str] = Depends(api_key_header)):
    allowed_keys = [
        k.strip()
        for k in os.getenv("API_KEYS", "").split(",")
        if k.strip()
    ]

    if not key or key not in allowed_keys:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )


# Modeli i të dhënave
class Item(BaseModel):
    name: str
    description: Optional[str] = None


# 1. Krijimi i një elementi
@app.post("/items/", dependencies=[Depends(check_key)], status_code=201)
def create_item(item: Item):
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, description) VALUES (?, ?)",
            (item.name, item.description)
        )

        return {
            "id": cursor.lastrowid,
            **item.model_dump()
        }


# 2. Marrja e të gjithë elementeve
@app.get("/items/", dependencies=[Depends(check_key)])
def get_items():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM items"
        ).fetchall()

        return [dict(row) for row in rows]


# 3. Marrja e një elementi sipas ID-së
@app.get("/items/{item_id}", dependencies=[Depends(check_key)])
def get_item(item_id: int):
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM items WHERE id = ?",
            (item_id,)
        ).fetchone()

        if row is None:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        return dict(row)


# 4. Përditësimi i një elementi
@app.put("/items/{item_id}", dependencies=[Depends(check_key)])
def update_item(item_id: int, item: Item):
    with get_db() as conn:
        cursor = conn.execute(
            """
            UPDATE items
            SET name = ?, description = ?
            WHERE id = ?
            """,
            (item.name, item.description, item_id)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        row = conn.execute(
            "SELECT * FROM items WHERE id = ?",
            (item_id,)
        ).fetchone()

        return dict(row)


# 5. Fshirja e një elementi
@app.delete("/items/{item_id}", dependencies=[Depends(check_key)])
def delete_item(item_id: int):
    with get_db() as conn:
        cursor = conn.execute(
            "DELETE FROM items WHERE id = ?",
            (item_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Item not found"
            )

        return {
            "message": "Item deleted successfully",
            "id": item_id
        }

@app.put("/items/{item_id}", dependencies=[Depends(check_key)])
def update_item(item:id, item:Item):
    with get_db() as conn:
        cursor = conn.execute(
            "UPDATE items SET name = ?, description = ?",(item.name,item.description,item.id)

        )
        if cursor.rowcount == 0:
            raise HTTPException(404, "Item not found")

        return {id:item.id, **item.model_dump()}

@app.delete("/items/{item_id}", dependencies=[Depends(check_key)])