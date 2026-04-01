FROM python:3.11-slim

WORKDIR /app

# Copia TUDO primeiro (garante que o requirements vai junto)
COPY . .

# Instala dependências (agora nunca falha)
RUN pip install --no-cache-dir -r requirements.txt

# Porta do Railway
ENV PORT=8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]