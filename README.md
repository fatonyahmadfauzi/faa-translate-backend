# 🌐 faa-translate-backend

📝 **faa-translate-backend** adalah backend API canggih untuk layanan penerjemahan berbasis AI menggunakan FastAPI dan model MarianMT. Dirancang untuk integrasi mudah dengan frontend atau digunakan secara independen.

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## ✨ Fitur Unggulan
- 🌍 Penerjemahan AI cerdas dengan **MarianMT**
- ⚡ Respons super cepat berkat **FastAPI & Gunicorn**
- 🔄 Dukungan 100+ kombinasi bahasa
- 📦 Fleksibel deploy di **Railway**, **Render**, atau **Docker**
- 🔒 Optimasi keamanan dan stabilitas

## 🚀 Teknologi Inti
| Komponen               | Teknologi                     |
|------------------------|-------------------------------|
| Framework API          | FastAPI                       |
| Mesin AI               | Hugging Face Transformers     |
| Optimasi Performa      | Gunicorn + Uvicorn            |
| Containerization       | Docker                        |

## 🛠️ Instalasi Lokal
### Prasyarat
- Python 3.9+
- Pip
- Git

### Langkah-langkah:
```bash
# 1️⃣ Clone repo
git clone https://github.com/[username]/faa-translate-backend.git
cd faa-translate-backend

# 2️⃣ Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau venv\Scripts\activate (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Jalankan server
uvicorn translate:app --host 0.0.0.0 --port 8000 --reload
