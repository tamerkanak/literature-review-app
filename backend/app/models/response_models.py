from pydantic import BaseModel
from typing import List, Dict

class LiteratureReviewResponse(BaseModel):
    literature_review: str
    message: str
    citations: List[Dict[str, str]] = []

class PDFProcessingResponse(BaseModel):
    filename: str
    content: str
    status: str 