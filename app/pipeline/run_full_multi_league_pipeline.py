from app.database import SessionLocal
from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches
from app.pipeline.generate_opportunities import generate_opportunities


def run_pipeline():

    print("🚀 INICIANDO PIPELINE...")

    db = SessionLocal()

    try:
        sync_leagues(db)
        sync_matches(db)
        generate_opportunities(db)  # 🔥 NOVO

        print("✅ PIPELINE FINALIZADO")

    except Exception as e:
        print("❌ ERRO NO PIPELINE:", e)

    finally:
        db.close()


