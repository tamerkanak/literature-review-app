import requests
from typing import List, Dict, Optional
import os
from .pdf_service import PDFService

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")

class LiteratureService:
    def __init__(self):
        self.pdf_service = PDFService()
    
    def generate_literature_review(self, research_topic: str, pdf_texts: List[str], output_language: str = "turkish", api_key: Optional[str] = None, embeddings=None) -> str:
        """Generate literature review based on research topic and PDF contents"""
        try:
            # Generate literature review using OpenRouter - one paragraph per paper
            literature_review = self._generate_with_openrouter(research_topic, pdf_texts, output_language, api_key)
            
            return literature_review
            
        except Exception as e:
            raise Exception(f"Error generating literature review: {str(e)}")
    
    def _generate_with_openrouter(self, research_topic: str, pdf_texts: List[str], output_language: str = "turkish", api_key: Optional[str] = None) -> str:
        """Generate literature review using OpenRouter API - one paragraph per paper"""
        try:
            # Set language instruction
            language_instruction = "Türkçe" if output_language == "turkish" else "English"
            
            system_prompt = f"""Sen akademik literatür taraması konusunda uzman bir araştırmacısın. Görevin, verilen araştırma konusu ve akademik makaleler temelinde kapsamlı bir "Literatür Taraması" bölümü yazmaktır.

ÖNEMLİ KURALLAR:
1. **SADECE "LİTERATÜR TARAMASI" BÖLÜMÜ**: Giriş ve Sonuç bölümleri yazma, sadece literatür taraması içeriği
2. **HER MAKALE İÇİN AYRI PARAGRAF**: Her makale için ayrı bir paragraf yaz
3. **SADECE O MAKALEYE REFERANS**: Her paragrafta sadece o makaleye referans ver
4. **APA 7 REFERANS FORMATI**: Metin içinde (Yazar, Yıl) formatında referans ver
5. **DOĞRU REFERANSLAR**: Sadece verilen kaynaklardan referans ver, uydurma referans kullanma
6. **MÜKEMMEL GRAMER**: Akıcı, doğru ve profesyonel {language_instruction} kullan
7. **AKADEMİK DİL**: Resmi, bilimsel ve profesyonel dil kullan
8. **KRİTİK ANALİZ**: Her makalenin bulgularını analiz et, güçlü ve zayıf yönlerini belirt

PARAGRAF YAPISI:
- Her makale için ayrı paragraf
- Her paragrafta sadece o makaleye referans ver
- Paragraf sonunda veya içinde (Yazar, Yıl) formatında referans
- Makalenin ana bulgularını, metodolojisini ve sonuçlarını analiz et
- Makalenin güçlü ve zayıf yönlerini belirt
- Araştırma konusuyla ilişkisini açıkla

DİL KALİTESİ:
- Mükemmel {language_instruction} gramer
- Akıcı ve doğal cümle yapıları
- Akademik terminoloji kullanımı
- Tutarlı zaman kullanımı
- Mantıklı paragraf geçişleri"""
            
            # Create context with paper numbers
            papers_context = ""
            for i, pdf_text in enumerate(pdf_texts, 1):
                papers_context += f"\n\nMAKALE {i}:\n{pdf_text[:2000]}..."  # Limit text length
            
            user_prompt = f"""ARAŞTIRMA KONUSU: {research_topic}

MEVCUT MAKALELER:
{papers_context}

Lütfen yukarıdaki araştırma konusu ve makaleler temelinde, SADECE "LİTERATÜR TARAMASI" bölümünü {language_instruction} dilinde yaz. Giriş ve Sonuç bölümleri yazma.

YAZIM GEREKSİNİMLERİ:
1. **Her Makale İçin Ayrı Paragraf**: Her makale için ayrı bir paragraf yaz
2. **Sadece O Makaleye Referans**: Her paragrafta sadece o makaleye referans ver
3. **APA 7 Referans Formatı**: (Yazar, Yıl) şeklinde metin içi referanslar
4. **Doğru Referanslar**: Sadece verilen kaynaklardan referans ver
5. **Mükemmel Gramer**: Akıcı ve doğru {language_instruction} kullan
6. **Kritik Analiz**: Her makalenin bulgularını analiz et
7. **Akademik Dil**: Profesyonel ve bilimsel üslup
8. **Mantıklı Akış**: Paragraflar arası geçişler tutarlı olsun

PARAGRAF İÇERİĞİ:
- Makalenin ana bulgularını detaylı açıkla
- Metodolojik yaklaşımını değerlendir
- Araştırma konusuyla ilişkisini belirt
- Makalenin güçlü ve zayıf yönlerini analiz et
- Paragraf sonunda veya içinde (Yazar, Yıl) formatında referans ver

LİTERATÜR TARAMASI:"""
            
            # API anahtarı önceliği: parametre > .env
            api_key_to_use = api_key if api_key else OPENROUTER_API_KEY
            
            headers = {
                "Authorization": f"Bearer {api_key_to_use}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": OPENROUTER_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": 1500,
                "temperature": 0.7
            }
            
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=180
            )
            response.raise_for_status()
            result = response.json()
            
            return result["choices"][0]["message"]["content"].strip()
            
        except Exception as e:
            raise Exception(f"Error calling OpenRouter API: {str(e)}")
    
    def _extract_citations(self, text: str) -> List[Dict[str, str]]:
        import re
        citations = []
        citation_pattern = r'\[(\d+)\]'
        matches = re.findall(citation_pattern, text)
        for match in matches:
            citations.append({
                "number": match,
                "type": "bracket"
            })
        return citations 