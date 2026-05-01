def predict_match_cards(match):
    team_a = match.home_team_id
    team_b = match.away_team_id

    avg_a = get_team_cards_avg(team_a)
    avg_b = get_team_cards_avg(team_b)

    conceded_a = get_team_cards_conceded_avg(team_a)
    conceded_b = get_team_cards_conceded_avg(team_b)

    base = (avg_a + conceded_b + avg_b + conceded_a) / 2

    # fator simples inicial (depois evoluímos)
    return base