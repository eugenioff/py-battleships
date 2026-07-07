import os

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

EXPECTED_TOKEN = os.environ["AUTH_TOKEN"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/secure")
def secure(authorization: str | None = Header(default=None)):
    if authorization != f"Bearer {EXPECTED_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {"status":"ok"}