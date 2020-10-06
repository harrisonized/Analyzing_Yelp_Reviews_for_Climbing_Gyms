import string
import re
import datetime as dt
import pandas as pd
import dask.bag as db


# Objects included in this file:

# Functions included in this file:
# # bag_to_df
# # flatten_review
# # preprocess_review_df
# # flatten_business
# # preprocess_business_df


def bag_to_df(bag, flatten=None, take=10000):
    """Converts bag to dataframe
    Make sure the take value is high enough but not too high
    """
    seq = bag.take(take)
    bag = db.from_sequence(seq, npartitions=1) # Converts back to bag for flattening
    if flatten:
        bag = bag.map(flatten)
    
    items = bag.take(take) # Grab important features
    df = pd.json_normalize(items)
    
    return df


def flatten_review(item):
    """Keys in review.json:
    ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date']
    Selectively filters out some of the keys
    """
    return {'date': item.get('date'),
            'business_id': item.get('business_id'),
            'useful': item.get('useful'),
            'funny': item.get('funny'),
            'cool': item.get('cool'),
            'text': item.get('text'),
            'stars': item.get('stars'), }


def preprocess_review_df(df):
    """Store all preprocessing functions here
    """
    df['date'] = df['date'].apply(lambda x : dt.datetime.strptime(x, "%m/%d/%Y"))
    df['text_length'] = df['text'].apply(len)
    df['text_clean'] = df.text.map(lambda x: re.sub(r'\w*\d\w*', ' ', x)).map(lambda x: re.sub(r'[%s]' % re.escape(string.punctuation), ' ', x.lower()))
    
    return df


def flatten_business(item):
    """Keys in business.json:
    ['business_id', 'link_id', 'name',
     'address', 'city','state', 'postal_code', 'telephone', 'latitude',  'longitude',
     'stars', 'review_count', 'is_open',
     'attributes', 'categories', 'hours']
    Selectively filters out some of the keys
    """
    return {'business_id': item.get('business_id'),
            'link_id': item.get('link_id'),
            'name': item.get('name'),
            'stars': item.get('stars'),
            'review_count': item.get('review_count'),
            'attributes': item.get('attributes'),
            'categories': item.get('categories'),
            'hours': item.get('hours'), }


def preprocess_business_df(df):
    """Store all preprocessing functions here
    """
    
    df.columns = df.columns.str.replace('attributes.', '').str.replace('hours.', '')
    df = df.rename(columns = {'stars': 'avg_stars'}) # Prevent conflict with review_df
    df = df.fillna(value = 0)
    df = df.replace(to_replace=['Yes', 'No'], value=[1, 0])
    
    return df


