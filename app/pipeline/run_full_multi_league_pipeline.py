from app.database import SessionLocal
from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches


def run_pipeline():

    print("🚀 INICIANDO PIPELINE...")

    db = SessionLocal()

    try:
        sync_leagues(db)
        sync_matches(db)

        print("✅ PIPELINE FINALIZADO")

    except Exception as e:
        print("❌ ERRO NO PIPELINE:", e)

    finally:
        db.close()


# 🚫 MUITO IMPORTANTE
# NÃO EXECUTAR AUTOMATICAMENTE
if __name__ == "__main__":
    run_pipeline()