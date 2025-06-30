# Literatür Tarama Uygulaması

Bu uygulama, araştırmacıların ve öğrencilerin literatür taraması yazım sürecini kolaylaştırmak için geliştirilmiş bir web uygulamasıdır. Kullanıcılar araştırma konularını belirtebilir, PDF formatında akademik makaleler yükleyebilir ve sistem otomatik olarak bilimsel dile uygun bir literatür taraması bölümü üretir.

**Geliştirici:** Tamer Kanak

## Özellikler

- **PDF Yükleme**: Maksimum 10 adet PDF dosyası yükleme
- **Metin Çıkarma**: PDF'lerden otomatik metin çıkarma
- **Vektörleştirme**: İçerikleri vektörel hale getirme (embedding)
- **Semantik Arama**: Cosine similarity ile benzerlik arama
- **LLM Entegrasyonu**: OpenRouter ile Claude 3.5 Sonnet modeli
- **Akademik Format**: Bilimsel dile uygun çıktı
- **Atıf Sistemi**: Hangi bilgilerin hangi kaynaklardan geldiğini belirtme
- **Çok Dilli Destek**: Türkçe ve İngilizce çıktı seçeneği
- **Her Makale İçin Ayrı Paragraf**: Her makale için ayrı analiz
- **Kullanıcı API Anahtarı**: Her kullanıcı kendi OpenRouter API anahtarını girebilir

## Teknolojiler

### Backend
- **Python FastAPI**: Web framework
- **PyMuPDF**: PDF işleme
- **OpenRouter API**: LLM entegrasyonu (Claude 3.5 Sonnet)
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

### OpenRouter API Anahtarı Alma
1. [OpenRouter.ai](https://openrouter.ai/) sitesine gidin
2. Ücretsiz hesap oluşturun
3. API anahtarınızı alın
4. Uygulamayı başlattıktan sonra arayüzdeki kutuya yapıştırın

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

5. `.env` dosyasını düzenleyin (API anahtarı kullanıcı arayüzünden de girilebilir):
```
OPENROUTER_API_KEY=dummy_key_here
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
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
2. OpenRouter API anahtarınızı arayüzdeki kutuya yapıştırın
3. Araştırma konunuzu ve amacınızı metin kutusuna yazın
4. Çıktı dilini seçin (Türkçe veya İngilizce)
5. PDF formatında akademik makalelerinizi yükleyin (maksimum 10 adet)
6. "Literatür Taraması Oluştur" butonuna tıklayın
7. Sistem işlemi tamamladığında oluşturulan literatür taramasını görüntüleyin
8. "Panoya Kopyala" butonu ile metni kopyalayabilirsiniz

## API Endpoints

### POST /upload-pdfs
PDF dosyalarını yüklemek için kullanılır.

### POST /generate-literature-review
Araştırma konusu, çıktı dili ve PDF dosyaları ile literatür taraması oluşturur. Kullanıcının API anahtarı header'da gönderilir.

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

Bu uygulama OpenRouter API üzerinden **Claude 3.5 Sonnet** modelini kullanır. Bu model:
- Yüksek kaliteli akademik metin üretimi
- Mükemmel gramer ve dil kalitesi
- Türkçe ve İngilizce destek
- Hızlı yanıt verir

## Özellikler

### Literatür Taraması Yapısı
- Her makale için ayrı paragraf
- Her paragrafta sadece o makaleye referans
- APA 7 formatında atıflar
- Kritik analiz ve sentez

### Çok Dilli Destek
- Türkçe çıktı seçeneği
- İngilizce çıktı seçeneği
- Dropdown menü ile kolay seçim

### Kullanıcı API Anahtarı Sistemi
- Her kullanıcı kendi OpenRouter API anahtarını girebilir
- API anahtarı localStorage'da saklanır
- Her istekte kullanıcının anahtarı kullanılır
- Güvenli ve kişiselleştirilmiş deneyim

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

**Geliştirici:** Tamer Kanak

Sorularınız için issue açabilir veya pull request gönderebilirsiniz. 
