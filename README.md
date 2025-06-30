# Literatür Tarama Uygulaması

Bu uygulama, araştırmacıların ve öğrencilerin literatür taraması yazım sürecini kolaylaştırmak için geliştirilmiş bir web uygulamasıdır. Kullanıcılar araştırma konularını belirtebilir, PDF formatında akademik makaleler yükleyebilir ve sistem otomatik olarak bilimsel dile uygun bir literatür taraması bölümü üretir.

## Özellikler

- **PDF Yükleme**: Maksimum 10 adet PDF dosyası yükleme
- **Metin Çıkarma**: PDF'lerden otomatik metin çıkarma
- **Vektörleştirme**: İçerikleri vektörel hale getirme (embedding)
- **Semantik Arama**: Cosine similarity ile benzerlik arama
- **LLM Entegrasyonu**: OpenRouter ile Llama 3.1-8B-Instruct modeli
- **Akademik Format**: Bilimsel dile uygun çıktı
- **Atıf Sistemi**: Hangi bilgilerin hangi kaynaklardan geldiğini belirtme

## Teknolojiler

### Backend
- **Python FastAPI**: Web framework
- **PyMuPDF**: PDF işleme
- **OpenRouter API**: LLM entegrasyonu (Llama 3.1-8B-Instruct)
- **Sentence Transformers**: Embedding oluşturma
- **Scikit-learn**: Cosine similarity hesaplama
- **Uvicorn**: ASGI server

### Frontend
- **React**: UI framework
- **React Dropzone**: Dosya yükleme
- **Axios**: HTTP client
- **CSS3**: Styling

## Kurulum

### Gereksinimler
- Python 3.8+
- Node.js 16+
- OpenRouter API anahtarı (ücretsiz hesap)

### Backend Kurulumu

1. Backend dizinine gidin:
```bash
cd backend
```

2. Sanal ortam oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Environment dosyasını oluşturun:
```bash
cp env.example .env
```

5. `.env` dosyasını düzenleyin (API anahtarı zaten eklenmiş):
```
OPENROUTER_API_KEY=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
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct
HOST=0.0.0.0
PORT=8000
FRONTEND_URL=http://localhost:3000
```

6. Backend'i çalıştırın:
```bash
python run.py
```

### Frontend Kurulumu

1. Frontend dizinine gidin:
```bash
cd frontend
```

2. Bağımlılıkları yükleyin:
```bash
npm install
```

3. Frontend'i çalıştırın:
```bash
npm start
```

## Kullanım

1. Tarayıcınızda `http://localhost:3000` adresine gidin
2. Araştırma konunuzu ve amacınızı metin kutusuna yazın
3. PDF formatında akademik makalelerinizi yükleyin (maksimum 10 adet)
4. "Literatür Taraması Oluştur" butonuna tıklayın
5. Sistem işlemi tamamladığında oluşturulan literatür taramasını görüntüleyin
6. "Panoya Kopyala" butonu ile metni kopyalayabilirsiniz

## API Endpoints

### POST /upload-pdfs
PDF dosyalarını yüklemek için kullanılır.

### POST /generate-literature-review
Araştırma konusu ve PDF dosyaları ile literatür taraması oluşturur.

## Proje Yapısı

```
literature-review-app/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI uygulaması
│   │   ├── models/              # Pydantic modelleri
│   │   └── services/            # İş mantığı servisleri
│   ├── requirements.txt         # Python bağımlılıkları
│   └── env.example             # Örnek environment dosyası
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/          # React bileşenleri
│   │   ├── App.js              # Ana uygulama bileşeni
│   │   └── index.js            # Giriş noktası
│   └── package.json            # Node.js bağımlılıkları
└── README.md                   # Bu dosya
```

## LLM Modeli

Bu uygulama OpenRouter API üzerinden **Llama 3.1-8B-Instruct** modelini kullanır. Bu model:
- Açık kaynak ve ücretsiz
- Akademik metin üretiminde başarılı
- Türkçe ve İngilizce destekler
- Hızlı yanıt verir

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

Sorularınız için issue açabilir veya pull request gönderebilirsiniz. 