from dataclasses import dataclass
from datetime import datetime
from .value_objects import EmailAddress, Cleanliness, Bias

@dataclass
class Email:
    id: str
    body: str 
    timestamp: datetime
    cleanliness: Cleanliness
    bias: Bias