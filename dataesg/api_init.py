import requests
from dataesg.api_config import ApiConfig
from dataesg.connection import Connection

def connect(api_key,**kwargs):
    url = 'esg_data?apiKey={}&where=%7B%0A%0A%7D'.format(api_key)
    ApiConfig.api_key = api_key
    r = Connection.request('get', url)
    
    return r.status_code


