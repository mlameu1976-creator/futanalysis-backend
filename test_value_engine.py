from app.services.value_bet_engine import ValueBetEngine

prob = 0.67
odd = 1.90

result = ValueBetEngine.build_value_bet(prob, odd)

print(result)