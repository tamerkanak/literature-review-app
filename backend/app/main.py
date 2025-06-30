from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import List
import os
from dotenv import load_dotenv

from .services.pdf_service import PDFService
from .services.literature_service import LiteratureService
from .models.response_models import LiteratureReviewResponse

load_dotenv()

app = FastAPI(title="Literature Review API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
pdf_service = PDFService()
literature_service = LiteratureService()

@app.get("/")
async def root():
    return {"message": "Literature Review API is running"}

@app.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    """Upload PDF files for processing"""
    if len(files) > 10:
        raise HTTPException(status_code=400, detail="Maximum 10 PDF files allowed")
    
    try:
        # Process uploaded PDFs
        processed_pdfs = []
        for file in files:
            if not file.filename or not file.filename.lower().endswith('.pdf'):
                raise HTTPException(status_code=400, detail=f"File {file.filename} is not a PDF")
            
            content = await file.read()
            pdf_text = pdf_service.extract_text_from_pdf(content)
            processed_pdfs.append({
                "filename": file.filename,
                "content": pdf_text
            })
        
        return {"message": f"Successfully processed {len(processed_pdfs)} PDF files", "files": processed_pdfs}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-literature-review")
async def generate_literature_review(
    request: Request,
    research_topic: str = Form(...),
    output_language: str = Form("turkish"),
    files: List[UploadFile] = File(...)
):
    """Generate literature review based on research topic and uploaded PDFs"""
    if len(files) > 10:
        raise HTTPException(status_code=400, detail="Maximum 10 PDF files allowed")
    
    try:
        # Extract text from PDFs
        pdf_texts = []
        for file in files:
            if not file.filename or not file.filename.lower().endswith('.pdf'):
                raise HTTPException(status_code=400, detail=f"File {file.filename} is not a PDF")
            
            content = await file.read()
            text = pdf_service.extract_text_from_pdf(content)
            pdf_texts.append(text)
        
        # Kullanıcıdan gelen API anahtarını header'dan al
        api_key = request.headers.get('x-openrouter-api-key')
        
        # Generate literature review
        literature_review = literature_service.generate_literature_review(
            research_topic=research_topic,
            pdf_texts=pdf_texts,
            output_language=output_language,
            api_key=api_key
        )
        
        return LiteratureReviewResponse(
            literature_review=literature_review,
            message="Literature review generated successfully"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 