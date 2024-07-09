from dataclasses import dataclass
@dataclass
class User:
        name: str
        email: str
        password: str
        birthdate: str = None
        gender: str = None