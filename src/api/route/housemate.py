from fastapi import APIRouter
from src.common.models.housemate import Housemate

router = APIRouter(
    prefix="/housemate",
    tags=["Housemates"],
)


@router.get("/", response_model=list[Housemate])
async def get_housemates():
    # Placeholder implementation
    return []

@router.post("/", response_model=Housemate)
async def create_housemate(housemate: Housemate):
    # Placeholder implementation
    return housemate

@router.put("/{housemate_id}", response_model=Housemate)
async def update_housemate(housemate_id: int, housemate: Housemate):
    # Placeholder implementation
    return housemate

@router.delete("/{housemate_id}")
async def delete_housemate(housemate_id: int):
    # Placeholder implementation
    return {"detail": "Housemate deleted"}

@router.get("/{housemate_id}", response_model=Housemate)
async def get_housemate(housemate_id: int):
    # Placeholder implementation
    return Housemate(id=housemate_id, name="John Doe")

