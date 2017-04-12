from os import path
import pandas as pd
import sys
from sklearn.externals import joblib


def predict(inx):
    file_dir = path.dirname(__file__)
    imputer_path = path.join(file_dir, 'imputer_fit.pkl')
    reg_path = path.join(file_dir, 'reg_fit.pkl')
    imputer = joblib.load(imputer_path) 
    reg_fit = joblib.load(reg_path)
    
    cols = ['num_critic_for_reviews', 'duration', 'director_facebook_likes',
       'actor_3_facebook_likes', 'actor_1_facebook_likes', 'gross',
       'num_voted_users', 'cast_total_facebook_likes', 'facenumber_in_poster',
       'num_user_for_reviews', 'budget', 'title_year',
       'actor_2_facebook_likes', 'aspect_ratio', 'movie_facebook_likes']
    inx = inx.ix[:,cols]
    imputed = imputer.transform(inx)
    return reg_fit.predict(imputed)

def get_data_frame(inx):
    try:
        return pd.read_json(inx)
    except:
        return pd.read_json(inx, typ='series')

if __name__ == "__main__":
    inx = get_data_frame(sys.argv[1])
    predict(inx)