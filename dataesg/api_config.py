import os

class ApiConfig:
    api_key = None
    api_protocol = 'https://'
    base_url = "{}api.appery.io/rest/1/apiexpress/api/".format(api_protocol)
    use_retries = True
    number_of_retries = 5
    retry_backoff_factor = 0.5
    max_wait_between_retries = 8
    retry_status_codes = [429] + list(range(500, 512))
    verify_ssl = True

    
def save_key(apikey, filename=None):
    if filename == None:
        filename = os.path.join(os.path.expanduser('~'), '.dataesg_apiKey')
    
    f = open(filename, 'w')
    f.write(apikey)
    f.close()

    ApiConfig.api_key = apikey


def read_key(filename=None):
    if filename is None:
        filename = os.path.join(os.path.expanduser('~'), '.dataesg_apiKey')

    with open(filename, 'r') as f:
        apikey = f.read()

    if not apikey:
        raise ValueError("File '{}' is empty.".format(filename))

    ApiConfig.api_key = apikey
