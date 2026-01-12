FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates gnupg libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libcairo2 libdrm2 libxkbcommon0 libgbm1 libx11-xcb1 libxcomposite1 \
    libxdamage1 libxrandr2 libasound2 fonts-liberation libwoff1 libopus0 \
    libwebp6 libjpeg62-turbo libxcb1 libxss1 libxext6 build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN playwright install --with-deps

ENV PYTHONUNBUFFERED=1
