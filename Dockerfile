FROM python:3.11-slim

WORKDIR /app

# Copia só o necessário primeiro (otimiza cache do Docker)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Inicia o servidor (Railway injeta a variável PORT automaticamente)
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]"# cache bust" 
