from fastapi import FastAPI
from pydantic import BaseModel

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
    return {"status": "ok"}