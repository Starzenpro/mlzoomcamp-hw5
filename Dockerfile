FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

# Copy requirements and install
COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Copy application
COPY main.py .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
