import React, { useState } from 'react';
import LiteratureReviewForm from './components/LiteratureReviewForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="container">
          <h1>Literatür Tarama Uygulaması</h1>
          <p>Akademik makalelerinizden otomatik literatür taraması oluşturun</p>
        </div>
      </header>
      
      <main className="container">
        <LiteratureReviewForm />
      </main>
      
      <footer className="App-footer">
        <div className="container">
          <p>&copy; 2024 Literatür Tarama Uygulaması. Tüm hakları saklıdır.</p>
        </div>
      </footer>
    </div>
  );
}

export default App; 