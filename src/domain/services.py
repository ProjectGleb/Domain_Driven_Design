# This service contains operations that don't naturally fit within a single entity or value object.
#In this case, these operations prepare the email for classification but don't make the final spam determination.

import re
from .entities import Email
from .value_objects import Cleanliness, Bias, BiasType

class EmailPreprocessingService:
    @staticmethod
    #Cleanign the email body logic
    def clean_email(email: Email) -> Email:
        # Implement email cleaning logic here
        cleaned_body = re.sub(r'\s+', ' ', email.body)
        email.body = cleaned_body
        return email

    @staticmethod
    def detect_cleanliness(email: Email) -> Cleanliness:
        # Implement grammatical error detection logic here
        # For simplicity, let's count the number of misspelled words
        misspelled_words = len([word for word in email.body.split() if len(word) > 10])
        return Cleanliness(grammatical_errors=misspelled_words)

    @staticmethod
    def detect_bias(email: Email) -> Bias:
        # Implement bias detection logic here
        # For simplicity, let's use a keyword-based approach
        lower_body = email.body.lower()
        if "urgent" in lower_body or "immediately" in lower_body:
            return Bias(type=BiasType.DEMANDING, score=0.8)
        elif "buy" in lower_body or "discount" in lower_body:
            return Bias(type=BiasType.SALESY, score=0.6)
        elif "please" in lower_body or "thank you" in lower_body:
            return Bias(type=BiasType.FRIENDLY, score=0.4)
        else:
            return Bias(type=BiasType.NEUTRAL, score=0.2)
