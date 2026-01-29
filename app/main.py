# app/main.py
from fastapi import FastAPI
from app.models import TokenRequest
from app.allocator import TokenAllocator

app = FastAPI(title="OPD Token Allocation Engine")

allocator = TokenAllocator()

@app.post("/allocate")
def allocate_token(request: TokenRequest):
    return allocator.allocate(
        request.doctor_id,
        request.slot_id,
        request.source,
        request.capacity
    )
