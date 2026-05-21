# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal
OrbitType = Literal[
    "LEO",
    "ISS",
    "POLAR",
    "SSO",
    "ES-L1",
    "HEO"
]

LaunchSiteType = Literal[
    "CCAFS SLC 40",
    "KSC LC 39A",
    "VAFB SLC 4E"
]

class Falcon9Input(BaseModel):

    FlightNumber: int = Field(...,ge=1,description="Flight number")
    PayloadMass: float = Field(...,ge=0,le= 70000,description="Payload mass in kg")
    Flights: int = Field(...,ge=0,description="Number of booster flights")
    Block: float = Field(...,ge=1,le=5,description="Booster block version")
    ReusedCount: int = Field(...,ge=0,description="Number of times booster reused")
    Orbit: OrbitType = Field(...,description="Target orbit")
    LaunchSite: LaunchSiteType = Field(...,description="Launch site")
    Serial: str = Field(...,min_length=3,max_length=10,description="Booster serial")
    LandingPad: Optional[str] = Field(None,description="Landing pad identifier")
    GridFins: bool = Field(...,description="Grid fins enabled")
    Reused: bool = Field(...,description="Booster reused")
    Legs: bool = Field(...,description="Landing legs enabled")

    @field_validator("Serial")
    @classmethod
    def validate_serial(cls, value):
        if not value.startswith("B"):
            raise ValueError("Serial must start with 'B'")
        return value

    model_config = {
        "json_schema_extra": {
            "example": {
                "FlightNumber": 90,
                "PayloadMass": 5300,
                "Flights": 2,
                "Block": 5,
                "ReusedCount": 1,
                "Orbit": "LEO",
                "LaunchSite": "KSC LC 39A",
                "Serial": "B1058",
                "LandingPad": "5e9e3032383ecb6bb234e7ca",
                "GridFins": True,
                "Reused": True,
                "Legs": True
            }
        }
    }
