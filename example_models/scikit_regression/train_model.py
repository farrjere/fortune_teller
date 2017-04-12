import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import Imputer
from collections import defaultdict
from sklearn.externals import joblib
from os import path

file_dir = path.dirname(__file__)
data_path = path.join(file_dir, '..', 'movie_metadata.csv')
df = pd.read_csv(data_path)
y = df[['imdb_score']]
X = df.filter(regex='^(?!imdb_score$).*')
#Going to just keeps things simple and ignore non-numeric cols
#string_vals = X.select_dtypes(include=['object']).fillna('')
#fit = string_vals.apply(lambda x: d[x.name].fit_transform(x)
X = X.select_dtypes(exclude=['object'])
imputer = Imputer()
X = imputer.fit_transform(X)

reg = linear_model.LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)
reg.fit(X_train, y_train)

imputer_path = path.join(file_dir, 'imputer_fit.pkl')
fit_path = path.join(file_dir, 'reg_fit.pkl')
joblib.dump(imputer, imputer_path)
joblib.dump(reg, fit_path)
