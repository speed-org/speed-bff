from dataclasses import dataclass


@dataclass
class RegisterPlayerDTO:
    name: str
    lastName: str
    email: str
    firebaseId: str
    refreshToken: str
