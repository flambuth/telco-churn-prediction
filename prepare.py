#Le jambon c'est un viande bonne
import numpy as np
import pandas as pd
# Import visualization modules
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder #OneHotEncoder, Imputer
#from sklearn.preprocessing import MinMaxScaler

import acquire

# def encode_variable(column, df):
#     lab_enc = LabelEncoder()
#     lab_enc.fit(df[column])
#     df[column] = lab_enc.transform(df[column])

def prep_telco():
    df = acquire.get_telco_chunk()
    df = df.set_index('customer_id')
#    df['churn'] = df['churn'].replace({'Yes':1,'No':0})
#    df['partner'] = df['partner'].replace({'Yes':1,'No':0})
#    df['dependents'] = df['dependents'].replace({'Yes':1,'No':0})
#    df['gender'] = df['gender'].replace({'Male':1,'Female':0})
    df['total_charges'] = df.total_charges.replace(' ', '0')
    df['total_charges'] = df.total_charges.astype('float')
    # encode_variable('online_security', df)
    # encode_variable('online_backup')
    # encode_variable('paperless_billing')
    # encode_variable('tech_support')
    # encode_variable('streaming_movies')
    # encode_variable('streaming_tv')
    # encode_variable('churn')
    # encode_variable('partner')
    # encode_variable('dependents')
    # encode_variable('gender')
    # encode_variable('phone_service')
    # encode_variable('multiple_lines')
    # encode_variable('device_protection')


    # df.online_backup = lab_enc.transform(df.online_backup)
    # df.device_protection = lab_enc.transform(df.device_protection)
    # df.tech_support = lab_enc.transform(df.tech_support)
    # df.streaming_tv = lab_enc.transform(df.streaming_tv)
    # df.streaming_movies = lab_enc.transform(df.streaming_movies)
    # df.paperless_billing = lab_enc.transform(df.paperless_billing)
    return df

# def encode_variable(column):
#     lab_enc = LabelEncoder()
#     lab_enc.fit(df[column])
#     df[column] = lab_enc.transform(df[column])


# Titanic Data

# # Use the function you defined in acquire.py to load the titanic data set.
# df_titanic = acquire.get_titanic_data()

# # Handle the missing values in the embark_town and embarked columns.
# df_titanic.embark_town.fillna('Other', inplace=True)

# # Remove the deck column.
# df_titanic.drop('deck', inplace=True, axis=1)

# # Use a label encoder to transform the embarked column.
# lab_enc = LabelEncoder()
# df_titanic.embarked.fillna('Unknown', inplace=True)
# lab_enc.fit(df_titanic.embarked)
# df_titanic.embarked = lab_enc.transform(df_titanic.embarked)

# # Scale the age and fare columns using a min max scaler. Why might this be beneficial? When might you not want to do this?
# scaler = MinMaxScaler()
# scaler2 = MinMaxScaler()

# # Would this work if it just included both ['fare','age'] in the fit or transform command?
# scaler.fit(df_titanic[['fare']])
# df_titanic.fare = scaler.transform(df_titanic[['fare']])

# scaler2.fit(df_titanic[['age']])
# df_titanic.age = scaler.transform(df_titanic[['age']])

#I'd like to add an imputation of something into the age column. It has some null values.
# def impute_titanic_age():
#     imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#     imputer = imputer.fit(df_titanic[['age']])
#     df_titanic['age'] = imputer.transform(df_titanic[['age']])

# imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# imputer = imputer.fit(df_titanic[['age']])
# imputer = imputer.fit(df_titanic[['age']])


# Create a function named prep_titanic that accepts the untransformed titanic data, and returns the data with the transformations above applied.
# def prep_titanic():
#     df_titanic = acquire.get_titanic_data()
#     df_titanic.embark_town.fillna('Other', inplace=True)
#     df_titanic.embarked.fillna('Unknown', inplace=True)
#     df_titanic.drop('deck', inplace=True, axis=1)
#     lab_enc = LabelEncoder()
#     lab_enc.fit(df_titanic.embarked)
#     df_titanic.embarked = lab_enc.transform(df_titanic.embarked)
#     scaler = MinMaxScaler()
#     scaler.fit(df_titanic[['fare','age']])
#     df_titanic.fare = scaler.transform(df_titanic[['fare', 'age']])
#     return df_titanic


#USE df.nunique()<5 instead of this temp list
# def pick_viable_categories(df):
#     discretes = df.select_dtypes(include='object')
#     temp = []
#     for column in discretes:
#         columnSeriesObj = discretes[column]
#         if len(columnSeriesObj.unique()) < 4:
#             temp.append(columnSeriesObj.name)
#     return temp

# def plot_viable_categories(target, df):
#     x = pick_viable_categories(df)
#     _, ax = plt.subplots(nrows=1, ncols=len(x), figsize=(16,5))
#     average_rate = df.target.mean()
#     for i, feature in enumerate(x):
#         sns.barplot(feature, target, data=df_titanic, ax=ax[i], alpha=.5)
#         ax[i].set_ylabel('average_rate')
#         ax[i].axhline(average_rate, ls='--', color='grey')

# def pick_viable_regressors():
#     regressors = df_titanic.select_dtypes(include=['float64','int64'])
#     temp = []
#     for column in regressors:
#         columnSeriesObj = regressors[column]
#         temp.append(columnSeriesObj.name)
#     return temp

def pick_numerical_columns(df):
    cont_cols = df.select_dtypes(include=['float64','int64'])
    temp = []
    for column in cont_cols:
        columnSeriesObj = cont_cols[column]
        temp.append(columnSeriesObj.name)
    return temp