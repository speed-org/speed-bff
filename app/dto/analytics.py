from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class AnalyticsEventDTO(BaseModel):
    event_type: str = Field(..., description="Type of the event")
    user_id: str = Field(..., description="User associated with the event")
    data: Optional[Dict[str, Any]] = Field(default_factory=lambda: {})
