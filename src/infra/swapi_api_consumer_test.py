from src.errors.http_request_error import HttpRequestError
from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships(requests_mock):
    ''' Testing get_starships method '''

    requests_mock.get('https://swapi.dev/api/starships/', 
    status_code=200, 
    json={'results': [{'name': 'Starship 1'}, {'name': 'Starship 2', 'results': [{'name': 'Starship 3'}]}]})

    swapi_api_consumer = SwapiApiConsumer()
    get_starships_response = swapi_api_consumer.get_starships(page=1)

    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == {'page': 1}
    
    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)

def test_get_starships_http_error(requests_mock):
    ''' Testing get starships method error in http request  '''

    requests_mock.get('https://swapi.dev/api/starships/', 
    status_code=404, 
    json={'detail': 'Not found'})

    swapi_api_consumer = SwapiApiConsumer()
    page=1000

    try:
        swapi_api_consumer.get_starships(page=page)
        assert True is False
    except HttpRequestError as e:
        assert e.message is not None
        assert e.status_code == 404
    

