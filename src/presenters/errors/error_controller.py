from typing import Type, Dict
from src.errors import HttpRequestError, HttpUnprocessableEntityError


def handler_erros(error: Type[Exception]) -> Dict:
    ''' 
        Handler to threat Exception cases
        @parm: error - Exception
        @return: Dict with data and statu_code
    '''

    if isinstance(error, HttpRequestError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
            }
    elif isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
            }
    else:
        return {
            "data": { "error": str(error) },
            "status_code": 500
         }
