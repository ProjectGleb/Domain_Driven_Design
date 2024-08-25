# Functions that combine the entities into an aggregate. It's a core business rule that determines whether an email is spam based on its properties.
#Aggregate root is the entity that is responsible for maintaining the consistency of the aggregate.

from dataclasses import dataclass
from .entities import Email

@dataclass
class EmailClassification:
    email: Email
    is_spam: bool

    def classify_spam(self):
        # Implement spam classification logic here
        # For now, let's use a simple rule: if the email has more than 5 grammatical errors or a demanding bias, it's spam
        if self.email.cleanliness.grammatical_errors > 5 or self.email.bias.type == "DEMANDING":
            self.is_spam = True
        else:
            self.is_spam = False