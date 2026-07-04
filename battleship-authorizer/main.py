import os

from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

EXPECTED_TOKEN = os.environ["AUTH_TOKEN"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/secure")
def secure(authorization: str | None = Header(default=None)):
    if authorization != f"Bearer {EXPECTED_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {"status":"ok"}