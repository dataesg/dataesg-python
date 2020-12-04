from dataesg.data import Dataset 
from dataesg.api_config import ApiConfig
from dataesg.database import request_data 
from dataesg.api_init import connect


def _check_inserted_type(param,msg):
    if len(param)==0:
        return []
    if isinstance(param, str):
        param = [param]
    elif isinstance(param, list) or isinstance(param, tuple):
        pass
    else:
        raise RuntimeError(msg)

    return param


def get_sample(metrics=[],return_format='pandas',**kwargs):

    metrics = _check_inserted_type(metrics,'Metrics must be specified as a string or list of strings')
    
    if 'api_key' in kwargs:
        ApiConfig.api_key = kwargs.pop('api_key')

    json_data = request_data({})
    data = Dataset(json_data,metrics)

    if return_format == 'numpy':
        return data.to_numpy()
    return data


def get_by_ticker(ticker,metrics=[],return_format='pandas',**kwargs):
    
    ticker = _check_inserted_type(ticker,'Ticker must be specified as a string or list of strings')
    metrics = _check_inserted_type(metrics,'Metrics must be specified as a string or list of strings')
    if len(ticker)==0:
        raise RuntimeError('ticker value is not specified')

    if 'api_key' in kwargs:
        ApiConfig.api_key = kwargs.pop('api_key')    

    json_data = request_data({'Ticker':ticker})

    if len(json_data)==0:
        raise RuntimeError('Value is not available under free package. Please contact us using the form in the website')

    data = Dataset(json_data,metrics)

    if return_format == 'numpy':
        return data.to_numpy()
    return data


def get_by_sedol(sedol,metrics=[],return_format='pandas',**kwargs):
    sedol = _check_inserted_type(sedol,'Sedol must be specified as a string or list of strings')
    metrics = _check_inserted_type(metrics,'Metrics must be specified as a string or list of strings')
    if len(sedol)==0:
        raise RuntimeError('sedol value is not specified')
    if 'api_key' in kwargs:
        ApiConfig.api_key = kwargs.pop('api_key')    

    json_data = request_data({'SEDOL':sedol})

    if len(json_data)==0:
        raise RuntimeError('Value is not available under free package. Please contact us using the form in the website')

    data = Dataset(json_data,metrics)

    if return_format == 'numpy':
        return data.to_numpy()
    return data


def get_by_isin(isin,metrics=[],return_format='pandas',**kwargs):
    isin = _check_inserted_type(isin, 'ISIN must be specified as a string or list of strings')
    metrics = _check_inserted_type(metrics, 'Metrics must be specified as a string or list of strings')
    if len(isin)==0:
        raise RuntimeError('isin value is not specified')

    if 'api_key' in kwargs:
        ApiConfig.api_key = kwargs.pop('api_key')  

    json_data = request_data({'ISIN':isin})

    if len(json_data)==0:
        raise RuntimeError('Value is not available under free package. Please contact us using the form in the website')
    
    data = Dataset(json_data,metrics)

    if return_format == 'numpy':
        return data.to_numpy()
    return data


def get_by_cusip(cusip,metrics=[],return_format='pandas',**kwargs):
    cusip = _check_inserted_type(cusip, 'Cusip must be specified as a string or list of strings')
    metrics = _check_inserted_type(metrics, 'Metrics must be specified as a string or list of strings')
    if len(cusip)==0:
        raise RuntimeError('cusip value is not specified')

    if 'api_key' in kwargs:
        ApiConfig.api_key = kwargs.pop('api_key')    

    json_data = request_data({'CUSIP':cusip})
    
    if len(json_data)==0:
        raise RuntimeError('Value is not available under free package. Please contact us using the form in the website')

    data = Dataset(json_data,metrics)

    if return_format == 'numpy':
        return data.to_numpy()
    return data



