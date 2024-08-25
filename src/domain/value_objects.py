
# These are immutable objects that represent concepts in the domain without a specific identity.

from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class EmailAddress:
    address: str

    def __post_init__(self):
        if not self._is_valid_email(self.address):
            raise ValueError("Invalid email address")

    @staticmethod
    def _is_valid_email(address: str) -> bool:
        # Implement email validation logic here
        return "@" in address

@dataclass(frozen=True)
class Cleanliness:
    grammatical_errors: int

class BiasType(Enum):
    DEMANDING = "demanding"
    SALESY = "salesy"
    FRIENDLY = "friendly"
    NEUTRAL = "neutral"

@dataclass(frozen=True)
class Bias:
    type: BiasType
    score: float

    def __post_init__(self):
        if not 0 <= self.score <= 1:
            raise ValueError("Bias score must be between 0 and 1")


