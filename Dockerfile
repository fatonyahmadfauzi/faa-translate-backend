# Gunakan image Python terbaru
FROM python:3.9

# Set direktori kerja
WORKDIR /app

# Copy semua file ke dalam container
COPY . .

# Buat virtual environment
RUN python -m venv venv

RUN pip install sentencepiece

# Aktifkan virtual environment dan install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Ekspos port 8080 (Cloud Run default)
EXPOSE 8080

# Gunakan virtual environment saat menjalankan aplikasi
CMD ["venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
