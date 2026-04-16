from app.database import SessionLocal
from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches
from app.pipeline.generate_opportunities import generate_opportunities

# 🔥 ADICIONE ISSO
from app.models import base
from sqlalchemy.orm import configure_mappers


def run_pipeline():

    print("🚀 INICIANDO PIPELINE...")

    # 🔥 GARANTE QUE O ORM ESTÁ PRONTO
    configure_mappers()

    db = SessionLocal()

    try:
        sync_leagues(db)
        sync_matches(db)
        generate_opportunities(db)

        print("✅ PIPELINE FINALIZADO")

    except Exception as e:
        print("❌ ERRO NO PIPELINE:", e)

    finally:
        db.close()