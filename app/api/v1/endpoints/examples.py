from fastAPI import APIRouter

router = APIRouter()

router.get("/")
async def get_all_examples():
    return [{"id": 1, "name": "example1", "description": "lorem ipsum"}]