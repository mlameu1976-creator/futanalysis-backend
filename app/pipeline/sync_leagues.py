from sqlalchemy import text


def sync_leagues(db):

    print("🚀 Inserindo ligas...")

    leagues = [
        (4328, "Premier League"),
        (4335, "La Liga"),
        (4332, "Serie A"),
        (4331, "Bundesliga"),
        (4334, "Ligue 1"),
        (4355, "Brasileirão"),
    ]

    inserted = 0

    for ext_id, name in leagues:

        db.execute(text("""
            INSERT INTO leagues (external_id, name, country)
            VALUES (:ext_id, :name, 'Unknown')
            ON CONFLICT (external_id) DO NOTHING
        """), {"ext_id": ext_id, "name": name})

        inserted += 1

    db.commit()

    print(f"✅ Ligas inseridas: {inserted}")