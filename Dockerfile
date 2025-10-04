FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency list first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Phidata Playground port
EXPOSE 7777

# Run the playground app
CMD ["python", "playground.py"]
