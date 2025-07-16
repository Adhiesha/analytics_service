from fastapi import APIRouter, Request
from app.services.clickhouse_client import insert_event
from datetime import datetime

router = APIRouter()

@router.post("")
async def track_event(request: Request):
    data = await request.json()
    event_type = data.get("eventType")
    payload = data.get("payload")
    timestamp = data.get("timestamp", int(datetime.utcnow().timestamp() * 1000))

    insert_event(event_type, payload, timestamp)
    return {"status": "ok"}
