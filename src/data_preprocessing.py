
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    # Create rating bins
    df.loc[(df['average_rating'] >= 0) & (df['average_rating'] <= 1), 'rating_between'] = "between 0 and 1"
    df.loc[(df['average_rating'] > 1) & (df['average_rating'] <= 2), 'rating_between'] = "between 1 and 2"
    df.loc[(df['average_rating'] > 2) & (df['average_rating'] <= 3), 'rating_between'] = "between 2 and 3"
    df.loc[(df['average_rating'] > 3) & (df['average_rating'] <= 4), 'rating_between'] = "between 3 and 4"
    df.loc[(df['average_rating'] > 4) & (df['average_rating'] <= 5), 'rating_between'] = "between 4 and 5"

    # One-hot encoding
    rating_df = pd.get_dummies(df['rating_between'])
    language_df = pd.get_dummies(df['language_code'])

    # Combine features
    features = pd.concat([rating_df, language_df, df['average_rating'], df['ratings_count']], axis=1)

    # Normalize features
    min_max_scaler = MinMaxScaler()
    features = min_max_scaler.fit_transform(features)

    return features