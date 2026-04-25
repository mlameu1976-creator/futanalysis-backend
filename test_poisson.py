from app.services.poisson import PoissonModel

def run_test():

    # exemplo de jogo
    home_xg = 1.6
    away_xg = 1.2

    result = PoissonModel.calculate_probabilities(home_xg, away_xg)

    print("\n==== TESTE POISSON FUTANALYSIS ====\n")

    for k, v in result.items():
        print(f"{k}: {round(v,4)}")

    print("\n===============================\n")


if __name__ == "__main__":
    run_test()