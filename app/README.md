
# OPD Token Allocation Engine

## Overview
    This project implements a backend token allocation system for a hospital OPD (Outpatient Department).
    It assigns patient tokens to doctors’ time slots while enforcing hard capacity limits, priority rules,
    and dynamic reallocation for real-world scenarios such as emergencies.
    
    The system is built as a REST API using FastAPI and demonstrates clean backend design,
    scalability concepts, and real-world reasoning.

---

## Problem Statement
    Doctors operate in fixed time slots (e.g., 9–10, 10–11), each with a maximum capacity.
    Tokens can originate from:
    - Online booking
    - Walk-in patients
    - Paid priority patients
    - Follow-up patients
    - Emergency cases

    The system must:
    - Enforce per-slot capacity limits
    - Prioritize higher-priority patients
    - Dynamically reallocate tokens
    - Handle real-world constraints reliably

---

## Priority Order
    Lower number indicates higher priority.
    
    | Priority | Source |
    |--------|--------|
    | 0 | Emergency |
    | 1 | Paid |
    | 2 | Follow-up |
    | 3 | Online |
    | 4 | Walk-in |

---

## Key Features
    - REST API for OPD token allocation
    - Hard per-slot capacity enforcement
    - Emergency override with dynamic reallocation
    - Predictable and explainable allocation logic
    - Swagger UI for API testing
    - Clean multi-file backend structure

---

## API Endpoint

### Allocate Token
**POST** `/allocate`

#### Request Body
```json
{
  "doctor_id": "D1",
  "slot_id": "D1-9-10",
  "source": "ONLINE",
  "capacity": 2
}
```

#### Responses

**Allocated**
```json
{
  "status": "ALLOCATED",
  "token_id": "uuid"
}
```

**Reallocated (Emergency override)**
```json
{
  "status": "REALLOCATED",
  "removed_token": "uuid",
  "token_id": "uuid"
}
```

**Rejected**
```json
{
  "status": "REJECTED",
  "reason": "Lower priority"
}
```

---

## Project Structure
```
Medoc Health/
├── app/
│   ├── __init__.py
│   ├── main.py        
│   ├── allocator.py    
│   ├── models.py      
│   └── simulation.py  
├── requirements.txt
└── README.md
```

---

## Tech Stack
    - Python 3
    - FastAPI
    - Uvicorn
    - Pydantic
    - In-memory data structures

---

## How to Run

1. Activate virtual environment:
```bash
.\.venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start server:
```bash
python -m uvicorn app.main:app --reload
```

4. Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## Simulation
    A one-day OPD simulation with multiple doctors is included.

Run:
```bash
python app/simulation.py
```

---

## Design Decisions & Trade-offs
    - In-memory storage used for simplicity and clarity
    - Stateless API design for scalability
    - Explicit prioritization for transparency

---

## Conclusion
    This project demonstrates a production-oriented backend design approach,
    handling real-world healthcare workflows with correctness, reliability,
    and extensibility in mind.
