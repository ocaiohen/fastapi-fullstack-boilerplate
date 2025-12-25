from fastapi import APIRouter
from .endpoints import examples

v1_router = APIRouter()
v1_router.include_router(examples.router, prefix="/examples", tags=["Examples"])