from app.database import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE opportunities ADD COLUMN kickoff DATETIME;"))
    conn.commit()

print("✅ Coluna kickoff criada no banco correto")
