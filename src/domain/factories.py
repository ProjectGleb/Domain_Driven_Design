from .entities import Email
from .value_objects import Cleanliness, Bias, BiasType
from datetime import datetime
import uuid

class EmailFactory:
    @staticmethod
    def create(body: str) -> Email:
        return Email(
            id=str(uuid.uuid4()),
            body=body,
            timestamp=datetime.now(),
            cleanliness=Cleanliness(grammatical_errors=0),
            bias=Bias(type=BiasType.NEUTRAL, score=0.0)
        )

class EmailClassificationFactory:
    @staticmethod
    def create(email: Email, is_spam: bool) -> EmailClassification:
        return EmailClassification(email=email, is_spam=is_spam)

# Abstract class defines the interface for saving, retrieving, and listing emails and classifications.


