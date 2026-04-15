from sqlalchemy import text


def generate_opportunities(db):

    print("🚀 Gerando oportunidades...")

    matches = db.execute(text("SELECT id FROM matches")).fetchall()

    total = 0

    for m in matches:

        probability = 0.55
        odds = 2.0
        ev = (probability * odds) - 1

        db.execute(text("""
            INSERT INTO opportunities (match_id, market, probability, odds, ev)
            VALUES (:match_id, 'home_win', :p, :o, :ev)
            ON CONFLICT DO NOTHING
        """), {
            "match_id": m.id,
            "p": probability,
            "o": odds,
            "ev": ev
        })

        total += 1

    db.commit()

    print(f"✅ Oportunidades: {total}")