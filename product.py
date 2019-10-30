
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from scipy import stats

#Your env should be your own DB credentials.
import env 
import acquire
import prepare
import model

#Function goes here because I had trouble using it in a module and importing it.
def encode_variable(column, df):
    lab_enc = LabelEncoder()
    lab_enc.fit(df[column])
    df[column] = lab_enc.transform(df[column])

df = prepare.prep_telco()

cat_cols = df.select_dtypes('object').columns
for i in cat_cols:
    encode_variable(i, df)

important_feats = [
 'contract_type_id',
 'online_security',
 'tenure',
 'total_charges',
 'monthly_charges']

X = df[important_feats]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=123)

clf = DecisionTreeClassifier(criterion='gini', max_depth=7, random_state=123)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_train)
y_pred_proba = clf.predict_proba(X_train)