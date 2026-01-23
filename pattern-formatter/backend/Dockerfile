FROM python:3.11-slim

# Install LibreOffice and other dependencies
RUN apt-get update && apt-get install -y \
    FROM python:3.11-slim

    # Install LibreOffice and other dependencies
    RUN apt-get update && apt-get install -y \
        libreoffice \
        libreoffice-writer \
        && rm -rf /var/lib/apt/lists/*

    # Set working directory
    WORKDIR /app

    # Copy requirements first for caching (from backend directory)
    COPY backend/requirements.txt .

    # Install Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the backend application
    COPY backend/ .

    # Copy the frontend
    COPY frontend/ ./frontend/

    # Copy Cover Pages templates (use JSON array form to handle spaces in filenames)
    COPY ["Cover Pages/", "Cover Pages/"]

    # Create necessary directories
    RUN mkdir -p outputs uploads templates instance "outputs/Cover Pages"

    # Expose port
    EXPOSE 10000

    # Run the application
    CMD ["gunicorn", "pattern_formatter_backend:app", "--bind", "0.0.0.0:10000"]
