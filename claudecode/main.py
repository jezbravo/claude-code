from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from .database import get_db
from .models.app import App
from .schemas.app import AppCreate, AppResponse, AppUpdate

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


@app.post("/apps/", response_model=AppResponse)
async def create_app(app_data: AppCreate, db: AsyncSession = Depends(get_db)):
    db_app = App(**app_data.model_dump())
    db.add(db_app)
    await db.commit()
    await db.refresh(db_app)
    return db_app


@app.get("/apps/", response_model=List[AppResponse])
async def read_apps(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(App).offset(skip).limit(limit))
    apps = result.scalars().all()
    return apps


@app.get("/apps/{app_id}", response_model=AppResponse)
async def read_app(app_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(App).where(App.id == app_id))
    app = result.scalar_one_or_none()
    if app is None:
        raise HTTPException(status_code=404, detail="App not found")
    return app


@app.put("/apps/{app_id}", response_model=AppResponse)
async def update_app(app_id: int, app_update: AppUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(App).where(App.id == app_id))
    app = result.scalar_one_or_none()
    if app is None:
        raise HTTPException(status_code=404, detail="App not found")
    
    update_data = app_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(app, field, value)
    
    await db.commit()
    await db.refresh(app)
    return app


@app.delete("/apps/{app_id}")
async def delete_app(app_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(App).where(App.id == app_id))
    app = result.scalar_one_or_none()
    if app is None:
        raise HTTPException(status_code=404, detail="App not found")
    
    await db.delete(app)
    await db.commit()
    return {"message": "App deleted successfully"}