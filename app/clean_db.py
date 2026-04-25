from sqlalchemy import text
from app.database import SessionLocal, engine
from app.models.league import League

def clean_leagues():
    """Limpa a tabela de ligas"""
    db = SessionLocal()
    try:
        # Deletar todas as ligas
        db.query(League).delete()
        db.commit()
        print("✅ Tabela 'leagues' limpa com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao limpar: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    clean_leagues()
