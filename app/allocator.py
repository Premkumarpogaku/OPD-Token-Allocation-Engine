import heapq
import uuid

PRIORITY_MAP = {
    "EMERGENCY": 0,
    "PAID": 1,
    "FOLLOW_UP": 2,
    "ONLINE": 3,
    "WALK_IN": 4
}

class TokenAllocator:
    def __init__(self):
        self.slots = {}  # slot_id -> heap

    def allocate(self, doctor_id, slot_id, source, capacity):
        priority = PRIORITY_MAP[source]
        token_id = str(uuid.uuid4())

        # NEGATIVE priority for max-priority behavior
        token = (-priority, token_id, source)

        if slot_id not in self.slots:
            self.slots[slot_id] = []

        heap = self.slots[slot_id]

        # Slot has space
        if len(heap) < capacity:
            heapq.heappush(heap, token)
            return {"status": "ALLOCATED", "token_id": token_id}

        # Slot full → check lowest priority token
        lowest = min(heap)

        if token[0] > lowest[0]:  # higher priority arrives
            heap.remove(lowest)
            heapq.heapify(heap)
            heapq.heappush(heap, token)
            return {
                "status": "REALLOCATED",
                "removed_token": lowest[1],
                "token_id": token_id
            }

        return {
            "status": "REJECTED",
            "reason": "Lower priority"
        }
