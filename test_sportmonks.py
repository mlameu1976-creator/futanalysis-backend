from app.services.opportunity_service import OpportunityService

service = OpportunityService()
opportunities = service.get_opportunities()

print("Oportunidades encontradas:", len(opportunities))

for o in opportunities:
    print(
        o["league"],
        "|",
        o["home_team"],
        "x",
        o["away_team"],
        "| Over25:",
        round(o["metrics"]["combined"]["over_25_probability"], 2),
        "| BTTS:",
        round(o["metrics"]["combined"]["btts_probability"], 2),
    )
    