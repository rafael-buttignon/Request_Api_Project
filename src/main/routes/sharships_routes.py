from fastapi import APIRouter, Request as RequestFastApi
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
sharships_routes = APIRouter()

@sharships_routes.get("/api/starhips/list")
def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''


    get_pagination_validator(request)


    return { "Olá": "Mundo" }