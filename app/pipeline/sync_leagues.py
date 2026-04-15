from sqlalchemy.orm import Session
from app.models.league import League

# 🔥 LIGAS VALIDADAS (TheSportsDB)
VALID_LEAGUE_IDS = {
    4328: ("Premier League", "England"),
    4335: ("La Liga", "Spain"),
    4332: ("Serie A", "Italy"),
    4331: ("Bundesliga", "Germany"),
    4334: ("Ligue 1", "France"),
    4355: ("Brasileirão", "Brazil"),
    4346: ("MLS", "USA")
}


def sync_leagues(db: Session):
    print("\n🚀 [LEAGUES] Sincronizando...")

    added = 0

    for league_id, (name, country) in VALID_LEAGUE_IDS.items():

        league_id = int(league_id)

        exists = db.query(League).filter(
            League.external_id == league_id
        ).first()

        if exists:
            print(f"⏩ Liga já existe: {name}")
            continue

        league = League(
            name=name,
            country=country,
            external_id=league_id
        )

        db.add(league)
        added += 1

        print(f"✅ Liga inserida: {name}")

    db.commit()

    total = db.query(League).count()

    print(f"📊 Inseridas nesta execução: {added}")
    print(f"📊 Total no banco: {total}")

    # 🚨 VALIDAÇÃO REAL
    if total == 0:
        raise Exception("❌ Nenhuma liga no banco após sync")