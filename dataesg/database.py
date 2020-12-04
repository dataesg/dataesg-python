from dataesg.api_config import ApiConfig
from dataesg.connection import Connection
import requests

def request_data(param):
    json = []
    if param:
        for key,values in param.items():
            pass
        for value in values:
            url = "/esg_data?apiKey={}&where=%7B%0A%20%20%20%20%22{}%22%3A%20%22{}%22%0A%0A%7D".format(ApiConfig.api_key,key,value)
            r = Connection.request('get', url)
            json+=r.json()
    else:
        url = "/esg_data?apiKey={}&where=%7B%0A%7D".format(ApiConfig.api_key)
        r = Connection.request('get', url)
        json = r.json()

    return json
