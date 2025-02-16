from pydantic import BaseModel
from typing import Optional

class Complaint(BaseModel):
    complaintId: str
    category: str
    description: str
    victim: Optional[str] = None
    suspect: Optional[str] = None
    location: Optional[dict] = None  # {"lat": float, "lon": float}