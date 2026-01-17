from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.core import get_db

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "OK"}

@app.get("/db/health")
async def db_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"db": "OK"}
