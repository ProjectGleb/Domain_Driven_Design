from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Email
from .aggregates import EmailClassification

class EmailRepository(ABC):
    @abstractmethod
    def save(self, email: Email) -> None:
        pass

    @abstractmethod
    def get_by_id(self, email_id: str) -> Optional[Email]:
        pass

    @abstractmethod
    def get_all(self) -> List[Email]:
        pass

class ClassificationRepository(ABC):
    @abstractmethod
    def save(self, classification: EmailClassification) -> None:
        pass

    @abstractmethod
    def get_by_email_id(self, email_id: str) -> Optional[EmailClassification]:
        pass

    @abstractmethod
    def get_all(self) -> List[EmailClassification]:
        pass