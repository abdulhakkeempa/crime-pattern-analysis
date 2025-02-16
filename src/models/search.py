from pydantic import BaseModel
from typing import Optional

class SearchRequest(BaseModel):
    description: str
    victim: Optional[str] = None
    suspect: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    radius_km: Optional[float] = None
    top_k: int = 3
