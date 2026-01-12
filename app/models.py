from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class MatchInDB(BaseModel):
    source: str
    player: str
    opponent: str
    competition: Optional[str] = None
    date: Optional[datetime] = None
    score: Optional[str] = None
    url: Optional[str] = None
    external_id: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None
    scraped_at: Optional[datetime] = None

class RecentMatchesRequest(BaseModel):
    player1: str = Field(..., description="Имя первого игрока")
    player2: str = Field(..., description="Имя второго игрока")
    sport: Optional[str] = "table_tennis"
    blocking: Optional[bool] = False
    max_matches: Optional[int] = 20
