import React, { useState, useCallback, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import './LiteratureReviewForm.css';

const LiteratureReviewForm = () => {
  const [researchTopic, setResearchTopic] = useState('');
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [literatureReview, setLiteratureReview] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [outputLanguage, setOutputLanguage] = useState('turkish');
  const [apiKey, setApiKey] = useState('');

  // API anahtarını localStorage'dan yükle
  useEffect(() => {
    const storedKey = localStorage.getItem('openrouter_api_key') || '';
    setApiKey(storedKey);
  }, []);

  // API anahtarı değişince localStorage'a kaydet
  useEffect(() => {
    if (apiKey) {
      localStorage.setItem('openrouter_api_key', apiKey);
    }
  }, [apiKey]);

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length + uploadedFiles.length > 10) {
      setError('Maksimum 10 PDF dosyası yükleyebilirsiniz.');
      return;
    }

    const newFiles = acceptedFiles.map(file => ({
      file,
      id: Math.random().toString(36).substr(2, 9),
      name: file.name,
      size: file.size
    }));

    setUploadedFiles(prev => [...prev, ...newFiles]);
    setError('');
  }, [uploadedFiles]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf']
    },
    multiple: true
  });

  const removeFile = (fileId) => {
    setUploadedFiles(prev => prev.filter(f => f.id !== fileId));
  };

  const generateLiteratureReview = async () => {
    if (!apiKey.trim()) {
      setError('Lütfen OpenRouter API anahtarınızı girin.');
      return;
    }
    if (!researchTopic.trim()) {
      setError('Lütfen araştırma konunuzu girin.');
      return;
    }
    if (uploadedFiles.length === 0) {
      setError('Lütfen en az bir PDF dosyası yükleyin.');
      return;
    }
    setIsLoading(true);
    setError('');
    setSuccess('');
    try {
      // Create FormData for file upload
      const formData = new FormData();
      formData.append('research_topic', researchTopic);
      formData.append('output_language', outputLanguage);
      uploadedFiles.forEach((fileObj) => {
        formData.append('files', fileObj.file);
      });
      const response = await axios.post('/generate-literature-review', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'x-openrouter-api-key': apiKey
        },
      });
      setLiteratureReview(response.data.literature_review);
      setSuccess('Literatür taraması başarıyla oluşturuldu!');
    } catch (err) {
      console.error('Error generating literature review:', err);
      setError(err.response?.data?.detail || 'Literatür taraması oluşturulurken bir hata oluştu.');
    } finally {
      setIsLoading(false);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(literatureReview).then(() => {
      setSuccess('Metin panoya kopyalandı!');
    }).catch(() => {
      setError('Metin kopyalanırken bir hata oluştu.');
    });
  };

  return (
    <div className="literature-review-form">
      {/* API Key Information */}
      <div className="card info-card">
        <h2>⚠️ Önemli Bilgi</h2>
        <div className="info-content">
          <p><strong>Bu uygulama OpenRouter API kullanmaktadır.</strong></p>
          <p>Kendi API anahtarınızı almanız gerekiyor:</p>
          <ol>
            <li><a href="https://openrouter.ai/" target="_blank" rel="noopener noreferrer">OpenRouter.ai</a> sitesine gidin</li>
            <li>Ücretsiz hesap oluşturun</li>
            <li>API anahtarınızı alın</li>
            <li>Aşağıdaki kutuya yapıştırın</li>
          </ol>
          <p><em>Not: Ücretsiz plan günlük belirli sayıda istek hakkı verir.</em></p>
        </div>
        <div className="api-key-input-group">
          <label htmlFor="api-key-input">OpenRouter API Anahtarınız:</label>
          <input
            id="api-key-input"
            type="text"
            className="form-control api-key-input"
            value={apiKey}
            onChange={e => setApiKey(e.target.value)}
            placeholder="sk-or-..."
            autoComplete="off"
          />
        </div>
      </div>
      {/* Research Topic Section */}
      <div className="card">
        <h2>Araştırma Konusu</h2>
        <div className="form-group">
          <label className="form-label">
            Araştırma çalışmanızın konusunu ve amacını açıklayın:
          </label>
          <textarea
            className="form-control textarea"
            value={researchTopic}
            onChange={(e) => setResearchTopic(e.target.value)}
            placeholder="Örnek: Bu çalışmada, yapay zeka teknolojilerinin eğitim alanındaki uygulamalarını ve öğrenci performansına etkilerini inceleyeceğiz..."
            rows={4}
          />
        </div>
      </div>
      {/* Output Language Selection */}
      <div className="card">
        <h2>Çıktı Dili</h2>
        <div className="form-group">
          <label className="form-label">
            Literatür taramasının hangi dilde yazılmasını istiyorsunuz?
          </label>
          <select
            className="form-control"
            value={outputLanguage}
            onChange={(e) => setOutputLanguage(e.target.value)}
          >
            <option value="turkish">Türkçe</option>
            <option value="english">English</option>
          </select>
        </div>
      </div>
      {/* File Upload Section */}
      <div className="card">
        <h2>PDF Dosyaları Yükle</h2>
        <p className="upload-info">
          Literatür taraması yapmak istediğiniz akademik makaleleri yükleyin (maksimum 10 dosya)
        </p>
        <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
          <input {...getInputProps()} />
          {isDragActive ? (
            <p>Dosyaları buraya bırakın...</p>
          ) : (
            <p>PDF dosyalarını sürükleyip bırakın veya seçmek için tıklayın</p>
          )}
        </div>
        {/* Uploaded Files List */}
        {uploadedFiles.length > 0 && (
          <div className="uploaded-files">
            <h3>Yüklenen Dosyalar ({uploadedFiles.length}/10)</h3>
            <div className="file-list">
              {uploadedFiles.map((fileObj) => (
                <div key={fileObj.id} className="file-item">
                  <span className="file-name">{fileObj.name}</span>
                  <span className="file-size">({(fileObj.size / 1024 / 1024).toFixed(2)} MB)</span>
                  <button
                    type="button"
                    className="btn-remove"
                    onClick={() => removeFile(fileObj.id)}
                  >
                    ×
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
      {/* Generate Button */}
      <div className="card">
        <button
          className="btn btn-primary"
          onClick={generateLiteratureReview}
          disabled={isLoading || uploadedFiles.length === 0 || !researchTopic.trim() || !apiKey.trim()}
        >
          {isLoading ? 'Literatür Taraması Oluşturuluyor...' : 'Literatür Taraması Oluştur'}
        </button>
      </div>
      {/* Alerts */}
      {error && (
        <div className="alert alert-error">
          {error}
        </div>
      )}
      {success && (
        <div className="alert alert-success">
          {success}
        </div>
      )}
      {/* Loading Spinner */}
      {isLoading && (
        <div className="loading">
          <div className="spinner"></div>
        </div>
      )}
      {/* Literature Review Result */}
      {literatureReview && (
        <div className="card">
          <div className="result-header">
            <h2>Oluşturulan Literatür Taraması</h2>
            <button className="btn btn-secondary" onClick={copyToClipboard}>
              Panoya Kopyala
            </button>
          </div>
          <div className="literature-review-content">
            {literatureReview.split('\n').map((paragraph, index) => (
              <p key={index}>{paragraph}</p>
            ))}
          </div>
        </div>
      )}
      {/* Developer Info */}
      <div className="card developer-info">
        <p>Geliştirici: <strong>Tamer Kanak</strong></p>
      </div>
    </div>
  );
};

export default LiteratureReviewForm; 