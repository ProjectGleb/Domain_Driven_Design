from typing import List, Optional
from ..domain.entities import Email
from ..domain.aggregates import EmailClassification
from ..domain.repositories import EmailRepository, ClassificationRepository
from ..domain.factories import EmailFactory, EmailClassificationFactory

class InMemoryEmailRepository(EmailRepository):
    def __init__(self):
        self.emails = {}

    def add(self, email: Email) -> None:
        self.emails[email.id] = email

    def get_by_id(self, email_id: str) -> Optional[Email]:
        return self.emails.get(email_id)

    def get_all(self) -> List[Email]:
        return list(self.emails.values())

class InMemoryClassificationRepository(ClassificationRepository):
    def __init__(self):
        self.classifications = {}

    def add(self, classification: EmailClassification) -> None:
        self.classifications[classification.email.id] = classification

    def get_by_email_id(self, email_id: str) -> Optional[EmailClassification]:
        return self.classifications.get(email_id)

    def get_all(self) -> List[EmailClassification]:
        return list(self.classifications.values())