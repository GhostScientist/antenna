from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import WebSocket, WebSocketDisconnect
import json
import datetime
from fastapi.responses import HTMLResponse
import asyncio
import json

clients = set()

class MoveCommand(BaseModel):
    servo_id: int
    angle: float


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/move")
async def move(command: MoveCommand):
    print(f"Moving servo {command.servo_id} to angle {command.angle}")

    payload = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": "command_sent",
        "data": command.dict(),
    }

    print(f"Payload: {payload}")
    print(f"Clients: {len(clients)}")
    dead = []
    for ws in clients:
        try:
            await ws.send_text(json.dumps(payload))
        except:
            dead.append(ws)

    for ws in dead:
        clients.remove(ws)


@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    while True:
        # Simulate telemetry
        data = {
            "timestamp": "ts-123",
            "joints": [1.0, 2.0, 3.0]
        }
        await websocket.send_text(json.dumps(data))
        await asyncio.sleep(1)  # send every 1s
