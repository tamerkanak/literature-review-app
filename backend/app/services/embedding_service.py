import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Tuple
import os
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingService:
    def __init__(self):
        # Initialize sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def create_embeddings(self, texts: List[str]) -> np.ndarray:
        """Create embeddings for a list of texts"""
        try:
            # Create embeddings
            embeddings = self.model.encode(texts, convert_to_tensor=False)
            return embeddings
        except Exception as e:
            raise Exception(f"Error creating embeddings: {str(e)}")
    
    def find_similar_chunks(self, query: str, chunks: List[str], k: int = 5) -> List[str]:
        """Find most similar text chunks for a query using cosine similarity"""
        try:
            # Create embeddings for chunks
            chunk_embeddings = self.create_embeddings(chunks)
            
            # Create query embedding
            query_embedding = self.model.encode([query], convert_to_tensor=False)
            
            # Calculate cosine similarities
            similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
            
            # Get indices of top k similar chunks
            top_indices = np.argsort(similarities)[::-1][:k]
            
            # Return relevant chunks
            relevant_chunks = [chunks[i] for i in top_indices]
            return relevant_chunks
            
        except Exception as e:
            raise Exception(f"Error finding similar chunks: {str(e)}")
    
    def get_relevant_context(self, research_topic: str, pdf_texts: List[str], max_chunks: int = 10) -> str:
        """Get relevant context from PDF texts based on research topic"""
        try:
            # Chunk the PDF texts
            all_chunks = []
            for pdf_text in pdf_texts:
                # Simple chunking by sentences
                sentences = pdf_text.split('. ')
                chunks = [s.strip() + '.' for s in sentences if len(s.strip()) > 50]
                all_chunks.extend(chunks)
            
            # Find most relevant chunks
            relevant_chunks = self.find_similar_chunks(research_topic, all_chunks, max_chunks)
            
            # Combine into context
            context = '\n\n'.join(relevant_chunks)
            return context
            
        except Exception as e:
            raise Exception(f"Error getting relevant context: {str(e)}") 