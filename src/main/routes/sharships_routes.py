from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_information_composer import get_starship_information_composer


sharships_routes = APIRouter()
@sharships_routes.get("/api/starhips/list")
async def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''

    get_pagination_validator(request)
    controller = get_starships_in_pagination_composer()

    response = await request_adapter(request, controller.handle)

    return JSONResponse(
        status_code= response["status_code"],
        content = {"data": response["data"]}
    )

# Essa rota fica melhor com get! "Pega informação de um determinado starship"
@sharships_routes.post("/api/starhips/information")
async def get_starship_information(request: RequestFastApi):
    ''' get_starship_information '''

    controller = get_starship_information_composer()

    response = await request_adapter(request, controller.handler)
    
    return JSONResponse(
        status_code= response["status_code"],
        content = {"data": response["data"]}
    )
