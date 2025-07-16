import os
import json
from clickhouse_driver import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(
    host=os.getenv("CLICKHOUSE_HOST"),
    port=int(os.getenv("CLICKHOUSE_PORT")),
    user=os.getenv("CLICKHOUSE_USER"),
    password=os.getenv("CLICKHOUSE_PASSWORD"),
    database=os.getenv("CLICKHOUSE_DB"),
)

def insert_event(event_type, payload, timestamp):
    query = """
        INSERT INTO web_analytics (eventType, payload, timestamp)
        VALUES
    """
    client.execute(query, [(event_type, json.dumps(payload), int(timestamp / 1000))])
