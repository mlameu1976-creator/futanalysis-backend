from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:452576@localhost:5432/futanalysis"

try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("✅ CONECTOU COM SUCESSO")
    conn.close()
except Exception as e:
    print("❌ ERRO:", e)