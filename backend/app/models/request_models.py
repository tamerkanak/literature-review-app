from pydantic import BaseModel
from typing import List
 
class LiteratureReviewRequest(BaseModel):
    research_topic: str
    pdf_contents: List[bytes]
    pdf_filenames: List[str] 