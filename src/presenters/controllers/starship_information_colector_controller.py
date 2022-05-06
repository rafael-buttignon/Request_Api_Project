from typing import Type, Dict
from src.presenters.interface.controllers_interface import ControllersInterface
from src.domain.usecases.starship_information_colector import StarshipsInformationColectorInterface

class StarshipInformationColectorController(ControllersInterface):

    ''' Handler to information colector controller '''

    def __init__(self, starship_information_colector: Type[StarshipsInformationColectorInterface]) -> None:
        self.__use_case = starship_information_colector

    def handler(self, http_request: Dict):
        ''' Handler to information colector controller '''
        starship_d = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__use_case.find_starship(starship_d, time)
        http_response = {"status_code": 200, "data": {"data": starship_information}}

        return http_response


