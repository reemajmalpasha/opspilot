# Stage 1: install dependencies
FROM python:3.12-slim-bookworm AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: small runtime image
FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app ./app
COPY runbooks ./runbooks
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]