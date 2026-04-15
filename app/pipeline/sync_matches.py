from sqlalchemy.orm import Session
from app.models.league import League
from app.services.thesportsdb_future_ingest_service import ingest_future_matches


def sync_matches(db: Session):
    print("\n🚀 [MATCHES] Sincronizando...")

    leagues = db.query(League).all()

    if not leagues:
        raise Exception("❌ Nenhuma liga encontrada antes de buscar jogos")

    created_total = 0

    for league in leagues:
        print(f"📡 Buscando jogos para liga_id={league.external_id}")

        created = ingest_future_matches(
            db=db,
            league_id=league.external_id  # 🔥 CRÍTICO
        )

        print(f"✔ Jogos inseridos para liga {league.name}: {created}")

        created_total += created

    print(f"\n📊 Total jogos inseridos: {created_total}")

    if created_total == 0:
        raise Exception("❌ Nenhum jogo foi inserido pelo ingest_future_matches")

    return created_total