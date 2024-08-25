#1. Dtos (Data Transfer Objects) allow to transfer data between different layers of the application. Allowing for decoupling and seperation of concerns.
#2. It allso allows you to shape and validate the data that is being trasferred.
#3. It Versioning: They make it easier to version your API, as you can create new DTOs for new versions without changing the domain model.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class EmailDTO:
    id: str
    body: str

@dataclass
class ClassificationResultDTO:
    email_id: str
    is_spam: bool
    cleanliness_score: int
    bias_type: str
    bias_score: float