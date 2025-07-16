from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.track import router as track_router

app = FastAPI()

# Allow all origins for simplicity (or specify your frontend domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["https://your-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(track_router, prefix="/track")
