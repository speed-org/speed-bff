from dataclasses import dataclass

@dataclass
class RegisterPlayerDTO:
    name: str
    last_name: str
    email: str
    firebase_id: str
    refreshToken: str
