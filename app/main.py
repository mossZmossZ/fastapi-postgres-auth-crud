from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.init_db import init_db

from app import  crud, auth


app = FastAPI()

# Allow all CORS for demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Routers
app.include_router(crud.router)
app.include_router(auth.router)


@app.on_event("startup")
def on_startup():
    init_db()