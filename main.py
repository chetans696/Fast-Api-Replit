from fastapi import FastAPI
# from routes.note import note
from routes.ai import ai
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.include_router(note)
app.include_router(ai)
