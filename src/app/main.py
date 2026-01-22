from fastapi import FastAPI, Depends
from fastapi_pagination import add_pagination
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.core import engine, get_db
from app.models import Base

from app.routers import itemsRoutes
from app.routers import wearRoutes

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routes defined from /routers dir
app.include_router(itemsRoutes.router, prefix="/items", tags=["items"])
app.include_router(wearRoutes.router, prefix="/wear", tags=["wear"])

add_pagination(app)
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

