from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from ..application.services import EmailClassificationService
from ..application.dtos import EmailDTO, ClassificationResultDTO
from ..domain.services import EmailPreprocessingService
from ..infrastructure.persistence import InMemoryEmailRepository, InMemoryClassificationRepository

app = FastAPI()

email_preprocessing_service = EmailPreprocessingService()
email_classification_service = EmailClassificationService(email_preprocessing_service)
email_repository = InMemoryEmailRepository()
classification_repository = InMemoryClassificationRepository()

class EmailInput(BaseModel):
    body: str

class ClassificationResult(BaseModel):
    email_id: str
    is_spam: bool
    cleanliness_score: int
    bias_type: str
    bias_score: float

@app.post("/classify_email", response_model=ClassificationResult)
async def classify_email(email_input: EmailInput):
    email_dto = EmailDTO(
        id=str(len(email_repository.get_all()) + 1),
        body=email_input.body,
        timestamp=datetime.now()
    )

    result = email_classification_service.classify_email(email_dto)

    # Save email and classification results
    email = Email(
        id=result.email_id,
        body=email_input.body,
        cleanliness=Cleanliness(grammatical_errors=result.cleanliness_score),
        bias=Bias(type=BiasType(result.bias_type), score=result.bias_score)
    )
    email_repository.save(email)

    classification = EmailClassification(email=email, is_spam=result.is_spam)
    classification_repository.save(classification)

    return ClassificationResult(
        email_id=result.email_id,
        is_spam=result.is_spam,
        cleanliness_score=result.cleanliness_score,
        bias_type=result.bias_type,
        bias_score=result.bias_score
    )

@app.get("/email/{email_id}", response_model=ClassificationResult)
async def get_email_classification(email_id: str):
    classification = classification_repository.get_by_email_id(email_id)
    if not classification:
        raise HTTPException(status_code=404, detail="Email classification not found")

    return ClassificationResult(
        email_id=classification.email.id,
        is_spam=classification.is_spam,
        cleanliness_score=classification.email.cleanliness.grammatical_errors,
        bias_type=classification.email.bias.type.value,
        bias_score=classification.email.bias.score
    )