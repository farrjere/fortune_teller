from os import path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import Imputer
from sklearn.externals import joblib


def main():
    file_dir = path.dirname(__file__)
    data_path = path.join(file_dir, '..', 'movie_metadata.csv')
    data_frame = pd.read_csv(data_path)
    y = data_frame[['imdb_score']]
    X = data_frame.filter(regex='^(?!imdb_score$).*')
    # Going to just keeps things simple and ignore non-numeric cols
    #string_vals = X.select_dtypes(include=['object']).fillna('')
    # fit = string_vals.apply(lambda x: d[x.name].fit_transform(x)
    X = X.select_dtypes(exclude=['object'])
    imputer = Imputer()
    X = imputer.fit_transform(X)

    reg = linear_model.LinearRegression()
    x_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.4, random_state=42)
    reg.fit(x_train, y_train)

    imputer_path = path.join(file_dir, 'imputer_fit.pkl')
    fit_path = path.join(file_dir, 'reg_fit.pkl')
    joblib.dump(imputer, imputer_path)
    joblib.dump(reg, fit_path)


if __name__ == "__main__":
    main()
