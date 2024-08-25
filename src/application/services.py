from ..domain.entities import Email
from ..domain.value_objects import Cleanliness, Bias, BiasType
from ..domain.aggregates import EmailClassification
from ..domain.services import EmailPreprocessingService
from ..domain.factories import EmailFactory, EmailClassificationFactory
from ..domain.repositories import EmailRepository, ClassificationRepository
from .dtos import EmailDTO, ClassificationResultDTO

class EmailClassificationService:
    def __init__(self, 
                 email_preprocessing_service: EmailPreprocessingService,
                 email_repository: EmailRepository,
                 classification_repository: ClassificationRepository):
        self.email_preprocessing_service = email_preprocessing_service
        self.email_repository = email_repository
        self.classification_repository = classification_repository

    def classify_email(self, email_dto: EmailDTO) -> ClassificationResultDTO:
        # Create Email entity using factory
        email = EmailFactory.create(
            body=email_dto.body,
            sender=email_dto.sender,
            recipient=email_dto.recipient,
            subject=email_dto.subject
        )

        # Preprocess email
        cleaned_email = self.email_preprocessing_service.clean_email(email)
        cleanliness = self.email_preprocessing_service.detect_cleanliness(cleaned_email)
        bias = self.email_preprocessing_service.detect_bias(cleaned_email)

        # Update email with preprocessed data
        cleaned_email.cleanliness = cleanliness
        cleaned_email.bias = bias

        # Create classification using factory
        email_classification = EmailClassificationFactory.create(cleaned_email)
        email_classification.classify_spam()

        # Save email and classification
        self.email_repository.add(cleaned_email)
        self.classification_repository.add(email_classification)

        # Create and return ClassificationResultDTO
        return ClassificationResultDTO(
            email_id=cleaned_email.id,
            is_spam=email_classification.is_spam,
            cleanliness_score=cleaned_email.cleanliness.grammatical_errors,
            bias_type=cleaned_email.bias.type.value,
            bias_score=cleaned_email.bias.score
        )