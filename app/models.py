# app/models.py
from pydantic import BaseModel

class TokenRequest(BaseModel):
    doctor_id: str
    slot_id: str
    source: str
    capacity: int
