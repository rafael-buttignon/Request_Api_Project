from cerberus import Validator

def get_pagination_validator(request: any):
    ''' get_starships_in_pagination_validator '''

    query_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1', '2', '3', '4'], 'required': True},
        'ola': {'type': 'string'}
    })

    response = query_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(query_param_validator.errors)

    