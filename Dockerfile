# Slim base = faster builds + smaller attack surface
FROM python:3.11-slim

# Don't write .pyc, don't buffer stdout (so Cloud Run logs are live)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /srv

# Install deps first so Docker layer caches them across rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY app ./app

EXPOSE 8080

# Cloud Run sends traffic to $PORT. gunicorn binds to it.
# 2 workers x 4 threads is conservative; tune later if needed.
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 --timeout 60 app.main:app
