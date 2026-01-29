# app/simulation.py
from app.allocator import TokenAllocator

allocator = TokenAllocator()

doctors = ["D1", "D2", "D3"]
slots = ["9-10", "10-11"]

for doctor in doctors:
    for i in range(5):
        result = allocator.allocate(
            doctor_id=doctor,
            slot_id=f"{doctor}-{slots[0]}",
            source="ONLINE",
            capacity=3
        )
        print(doctor, result)

# Emergency case
print("Emergency insertion:")
print(
    allocator.allocate(
        "D1",
        "D1-9-10",
        "EMERGENCY",
        3
    )
)
