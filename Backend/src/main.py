import json
from fastapi import FastAPI
from pydantic import BaseModel
from users.router import router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

