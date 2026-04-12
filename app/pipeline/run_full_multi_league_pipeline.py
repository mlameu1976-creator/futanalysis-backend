from app.database import SessionLocal
from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches
from app.pipeline.run_opportunity_pipeline import run_opportunity_pipeline


def main():

    print("🚀 INICIANDO PIPELINE COMPLETO")

    db = SessionLocal()

    try:
        print("📊 Sincronizando ligas...")
        sync_leagues(db)

        print("⚽ Sincronizando partidas...")
        sync_matches(db)

        print("💰 Gerando oportunidades...")
        run_opportunity_pipeline(db)

        print("✅ PIPELINE FINALIZADO COM SUCESSO")

    except Exception as e:
        print("❌ ERRO NO PIPELINE:", str(e))

    finally:
        db.close()