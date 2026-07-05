from dataclasses import dataclass
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import random
import requests

import fcn_game
import fcn_utils

app = FastAPI()

AUTH_URL = "http://ms-auth.local/secure"

@app.websocket("/ws")
async def websocket_test(ws: WebSocket):
    global total
    total= 0
    await ws.accept()

    await ws.send_text("WebSocket connection established.")
    await ws.send_text("Waiting for authentication message...")
    auth_msg = await ws.receive_json()
    token = auth_msg.get("token")

    auth_response = requests.get(AUTH_URL, headers={"Authorization": f"Bearer {token}"})

    if auth_response.status_code != 200:
        await ws.send_json({"error": "401 Unauthorized"})
        await ws.close()
        return
    
    try:
        while True:
            await ws.send_text("Please type an integer. Type 0 to exit.")
            data = await ws.receive_text()
            try:
                num=int(data)
            except ValueError:
                await ws.send_text("Invalid input. Please type an integer.")
                continue
        
            if num == 0:
                await ws.send_text("Exiting. Goodbye!")
                await ws.close()
                break

            total += num
            await ws.send_text(f"Current total: {total}")
    
    except WebSocketDisconnect:
        print("WebSocket connection closed.")