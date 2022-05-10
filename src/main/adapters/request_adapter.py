from typing import Callable
from fastapi import Request as RequestFastApi

async def request_adapter(request: RequestFastApi, callback: Callable):
    ''' request_adapter fast api adapter '''

    body = None
    
    try:
        body = await request.json()
    except:
        Exception("Error on request_adapter")

    http_request = {
        'query_params': request.query_params,
        'body': body
    }

    http_reponse = callback(http_request)
    return http_reponse

