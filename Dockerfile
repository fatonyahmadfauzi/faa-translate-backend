# Gunakan Python 3.9-slim sebagai base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin file requirements terlebih dahulu (untuk caching)
COPY requirements.txt .

# Install semua dependency termasuk SentencePiece dan PyTorch
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir torch torchvision torchaudio sentencepiece

# Salin semua file aplikasi ke dalam image
COPY . .

# Expose port untuk aplikasi FastAPI
EXPOSE 8080

# Jalankan aplikasi menggunakan Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
