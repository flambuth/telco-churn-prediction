#gathering data from SQL
import pandas as pd
import env 



def get_db_url(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_telco_chunk():
    query = '''
    SELECT 
    *
    FROM 
    customers
    ;
    '''
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df

def get_month2month():
    query = '''
    SELECT 
    *
    FROM 
    customers
    WHERE contract_type_id = 1
    AND tenure = 12
    ;
    '''
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df

def get_1year():
    query = '''
    SELECT 
    *
    FROM 
    customers
    WHERE contract_type_id = 2
    AND tenure = 12
    ;
    '''
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df

