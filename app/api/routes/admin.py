from fastapi import APIRouter

router = APIRouter()

# 🚫 DESATIVADO TEMPORARIAMENTE
@router.get("/admin")
def admin():
    return {"status": "admin desativado"}