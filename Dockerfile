FROM python:3.12-slim

# Install Firefox and Geckodriver dependencies
RUN apt-get update && apt-get install -y \
    wget \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver
RUN GECKODRIVER_VERSION=0.29.1 \
    && wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && tar -xzf geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz

# Copy the application files
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
