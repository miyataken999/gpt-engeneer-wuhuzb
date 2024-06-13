from fastapi import FastAPI
from database import engine, Base
from routers import user_router, team_router

app = FastAPI()

app.include_router(user_router)
app.include_router(team_router)

Base.metadata.create_all(bind=engine)