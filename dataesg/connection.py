import re
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from dataesg.api_config import ApiConfig


class Connection:
    @classmethod
    def request(cls, http_verb, url, **options):
        if 'headers' in options:
            headers = options['headers']
        else:
            headers = {}

        accept_value = 'application/json'

        headers = {'accept': accept_value,
                   'request-source': 'python',
                    }
        options['headers'] = headers

        abs_url = ApiConfig.base_url+url

        return cls.execute_request(http_verb, abs_url, **options)

    @classmethod
    def execute_request(cls, http_verb, url, **options):
        session = cls.get_session()
        if ApiConfig.api_key==None:
            raise RuntimeError("api_key is not specified")
        
        try:
            response = session.request(method=http_verb,
                                       url=url,
                                       verify=ApiConfig.verify_ssl,
                                       **options)
            if response.status_code < 200 or response.status_code >= 300:
                raise RuntimeError("Invalid api_key")
            else:
                return response
        except requests.exceptions.RequestException as e:
            raise e

    @classmethod
    def get_session(cls):
        session = requests.Session()
        adapter = HTTPAdapter(max_retries=cls.get_retries())
        session.mount(ApiConfig.api_protocol, adapter)

        return session

    @classmethod
    def get_retries(cls):
        if not ApiConfig.use_retries:
            return Retry(total=0)

        Retry.BACKOFF_MAX = ApiConfig.max_wait_between_retries
        retries = Retry(total=ApiConfig.number_of_retries,
                        connect=ApiConfig.number_of_retries,
                        read=ApiConfig.number_of_retries,
                        status_forcelist=ApiConfig.retry_status_codes,
                        backoff_factor=ApiConfig.retry_backoff_factor,
                        raise_on_status=False)

        return retries

