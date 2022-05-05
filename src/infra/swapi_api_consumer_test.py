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
    
def test_get_starship_infomation(requests_mock) -> None:
    ''' Testing get_starship_infomation method '''

    starship_id = 9

    swapi_api_consumer = SwapiApiConsumer()

    requests_mock.get(
        f"https://swapi.dev/api/starships/{starship_id}/",
        status_code=200,
        json={'name': 'some', 'model': 'thing', 'MGLT': '123'}
    )

    starship_information = swapi_api_consumer.get_starship_infomation(starship_id)

    assert starship_information.request.method == 'GET'
    assert starship_information.request.url == f"https://swapi.dev/api/starships/{starship_id}/"
    assert starship_information.status_code == 200

    assert "MGLT" in starship_information.response

def test_get_starship_infomation_error(requests_mock) -> None:
    ''' Testing get_starship_infomation method in error '''

    starship_id = 1

    swapi_api_consumer = SwapiApiConsumer()

    requests_mock.get(
        f"https://swapi.dev/api/starships/{starship_id}/",
        status_code=400,
        json={'detail': 'something'}
    )

    try:
        swapi_api_consumer.get_starship_infomation(starship_id=starship_id)
        assert True is False
    except HttpRequestError as e:
        assert e.message is not None
        assert e.status_code is not 200