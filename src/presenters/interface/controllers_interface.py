from typing import Dict
from abc import ABC, abstractmethod

class ControllersInterface(ABC):
    ''' ControllersInterface Interface'''

    @abstractmethod
    def handler(self, http_request: Dict):
        ''' Method to handle request '''
        raise 'Should implement handler method'