FROM python:3.11-slim

WORKDIR /app

# Copia tudo
COPY . /app

# DEBUG (vai mostrar arquivos no log)
RUN ls -la

# Instala dependências (se falhar, veremos no log)
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]