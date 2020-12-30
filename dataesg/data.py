import pandas as pd 
from dataesg.database import request_data 
import numpy as np
import warnings


def Dataset(json,metrics,years):
    df = pd.DataFrame.from_dict(json)
    df['Fiscal_Year'] = df['Fiscal_Year'].astype('float32').astype('int32')
    
    
    for column in df.columns:
        if column[0] == '_':
            df.drop(column,axis=1,inplace=True)
    df.replace('#N/A',np.nan,inplace=True)
    msg = 'Specified years are not available. All available years will be returned'
    if len(years)>0:
        if len(df[df['Fiscal_Year'].isin(years)])==0:
            warnings.warn(msg)
        else:
            df = df[df['Fiscal_Year'].isin(years)]
    
    columns = ['Company','Fiscal_Year','GRI_Framework','Ticker','ISIN','CUSIP']
    
    if 'SEDOL' in df.columns:
        columns.append('SEDOL')
    
    for column in df.columns:
        if column not in columns:
            df[column] = pd.to_numeric(df[column],errors='ignore',downcast='float')
   
    for m in metrics:
        if m in df.columns:
            columns.append(m)
        else:
            raise RuntimeError('{} is not available'.format(m))    

    if len(metrics)>0:
        return df[columns]

    return df