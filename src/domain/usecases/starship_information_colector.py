from abc import ABC, abstractclassmethod
from typing import Dict

class StarshipsInformationColectorInterface(ABC):

    ''' Starships Information Colector Interface'''

    @abstractclassmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        ''' Must implement '''
        raise Exception('Must implement find_starship method')