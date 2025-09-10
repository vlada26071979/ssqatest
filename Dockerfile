# ==========================
# Dockerfile za Selenium + pytest
# ==========================

FROM python:3.9-slim

# ==========================
# Instaliraj osnovne zavisnosti i Chrome dependencije
# ==========================
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# ==========================
# Instaliraj Google Chrome
# ==========================
RUN wget -q -O /usr/share/keyrings/google-linux-signing-key.gpg https://dl.google.com/linux/linux_signing_key.pub \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# ==========================
# Instaliraj ChromeDriver (Chrome for Testing)
# ==========================
RUN CHROMEDRIVER_VERSION=140.0.7339.82 && \
    wget -q "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /tmp/chromedriver-linux64


# ==========================
# Kopiraj projekat i instaliraj Python zavisnosti
# ==========================
WORKDIR /ssqatest
COPY . /ssqatest/

ENV PYTHONPATH=/ssqatest

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ==========================
# Postavi PYTHONPATH
# ==========================
ENV PYTHONPATH=/app

# ==========================
# Pokreni pytest kada se kontejner startuje
# ==========================
CMD ["pytest", "-v", "-s"]
