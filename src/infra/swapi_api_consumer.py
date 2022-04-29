from typing import Tuple, Type
from collections import namedtuple
from requests import Request
from src.errors import HttpRequestError
import requests

class SwapiApiConsumer:

    ''' Class to consume swapi api with http requests '''

    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')

    def get_starships(self, page: int) -> Tuple[int, Type[Request], dict]:

        ''' 
            Get starships from swapi api with pagination
            :parm - page: int with page of navegation
         :  :return - tuple with status code, request and response attributes
        '''

        req = requests.Request(
            method='GET',
            url="https://swapi.dev/api/starships/",
            params={'page': page}
            )
        req_prepared = req.prepare()
        
        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if(status_code != 200):
            raise HttpRequestError(
                message=response.json()['detail'],
                status_code=status_code
            )
        else:
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
    
    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:

        ''' 
            Prepare a session and send http requests
            :parm - req_prepared: Request object with all params
            :return: - Http response raw
        '''

        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response