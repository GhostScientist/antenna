from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import WebSocket, WebSocketDisconnect
import json
import datetime

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

    for ws in clients:
        await ws.send_text(json.dumps(payload))

    return {"status": "ok"}


@app.websocket("/ws/telemetry")
async def telemetry_stream(ws: WebSocket):
    await ws.accept()
    clients.add(ws)
    print("[antenna] Client connected to telemetry stream")

    try:
        while True:
            await ws.receive_text() 
    except WebSocketDisconnect:
        clients.remove(ws)
        print("[antenna] Client disconnected")