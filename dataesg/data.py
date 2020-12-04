import pandas as pd 
from dataesg.database import request_data 
import numpy as np
 
def Dataset(json,metrics):
    df = pd.DataFrame.from_dict(json)
    for column in df.columns:
        if column[0] == '_':
            df.drop(column,axis=1,inplace=True)
    df.replace('#N/A',np.nan,inplace=True)
    
    columns = ['Company','Fiscal_Year','GRI_Framework','Ticker','ISIN','CUSIP']
    if 'SEDOL' in df.columns:
        columns.append('SEDOL')
    for m in metrics:
        if m in df.columns:
            columns.append(m)
        else:
            raise RuntimeError('Metrics {} is not available'.format(m))    
    
    if len(metrics)>0:
        return df[columns]

    return df