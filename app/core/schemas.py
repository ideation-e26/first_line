from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class UserInput(BaseModel):
    text: str
    city: Optional[str] = "Quebec city"


class StructuredData(BaseModel):
    symptoms: List[str]
    duration: Optional[str]
    severity: Optional[str]
    risk_flags: List[str]
    demographics: Dict[str, Any]
    location: Dict[str, Any]
    uncertainty: float


class TriageData(BaseModel):
    urgency_level: str
    intent: str
    red_flags: List[str]


class Plan(BaseModel):
    actions: List[Dict[str, str]]
