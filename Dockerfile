FROM python:3.9-slim

WORKDIR /app

# Salin dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY . .

# Jalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "app.main:app"]
