
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder #OneHotEncoder, Imputer
#from sklearn.preprocessing import MinMaxScaler

import acquire

def encode_variable(column, df):
    lab_enc = LabelEncoder()
    lab_enc.fit(df[column])
    df[column] = lab_enc.transform(df[column])

def prep_telco():
    df = acquire.get_telco_chunk()
    df = df.set_index('customer_id')
    df['total_charges'] = df.total_charges.replace(' ', '0')
    df['total_charges'] = df.total_charges.astype('float')
    return df

def pick_numerical_columns(df):
    cont_cols = df.select_dtypes(include=['float64','int64'])
    temp = []
    for column in cont_cols:
        columnSeriesObj = cont_cols[column]
        temp.append(columnSeriesObj.name)
    return temp

#    df['churn'] = df['churn'].replace({'Yes':1,'No':0})
#    df['partner'] = df['partner'].replace({'Yes':1,'No':0})
#    df['dependents'] = df['dependents'].replace({'Yes':1,'No':0})
#    df['gender'] = df['gender'].replace({'Male':1,'Female':0})