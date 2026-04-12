# 🚫 NÃO EXECUTA AUTOMATICAMENTE

def run_pipeline():
    from app.pipeline.sync_leagues import sync_leagues
    from app.pipeline.sync_matches import sync_matches

    print("🚀 INICIANDO PIPELINE...")

    sync_leagues()
    sync_matches()

    print("✅ PIPELINE FINALIZADO")


# 🔥 SÓ EXECUTA SE RODAR DIRETO (LOCAL)
if __name__ == "__main__":
    run_pipeline()