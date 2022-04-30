
from collections import namedtuple
from faker import Faker

def mock_starships():
    ''' 
        mock data for starships 
        :return - dict with starships information
    '''

    fake = Faker()
    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": f"https://swapi.dev/api/starships/1/".format(fake.random_int())
    }

class SwapiApiConsumerSpy:

    ''' Spy for SwapiApiConsumer '''

    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
        self.get_starships_attributes = {}

    def get_starships(self, page: int) -> any:
        ''' mock to get starships list '''

        self.get_starships_attributes["page"] = page
        return self.get_starships_response(
            status_code=200, request=None, response={ "results": [mock_starships(), mock_starships() ] }
        )