@router.get("/cards")
def get_cards():
    return cards_prediction_service.get_all_predictions()