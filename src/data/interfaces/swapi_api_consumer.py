from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type
from requests import Request

class SwapiApiConsumerInterface(ABC):

    ''' Api Consumer interface '''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:

        ''' Must Implement '''

        raise Exception("Must implement get_starships method")


    @abstractmethod
    def get_starship_infomation(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:

        ''' Must Implement '''

        raise Exception("Must implement get_starship_infomation method")

