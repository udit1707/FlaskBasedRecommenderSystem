import numpy as np 
import pandas as pd 
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
#import linear kernel
from sklearn.metrics.pairwise import linear_kernel
import pymysql
from sqlalchemy import create_engine

cnx = create_engine('mysql+pymysql://b92e5f9aaa362f:cd35a5e2@us-cdbr-east-02.cleardb.com/heroku_32ef109f1d9bc84')    
# cnx = create_engine('mysql+pymysql://root:5511@localhost/trek-advisor')

#read data
treks = pd.read_sql_query("SELECT id,name,image,mean_rating,count_ratings FROM treks WHERE count_ratings>=1", cnx) #read the entire table
# print(treks.head())
C = treks['mean_rating'].mean()
#print(C)
m = treks['count_ratings'].quantile(0.)
print(m)
q_treks = treks.copy().loc[treks['count_ratings'] >= m]


def weighted_rating(x, m=m, C=C):
    v = x['count_ratings']
    R = x['count_ratings']
    return (v/(v+m) * R) + (m/(m+v) * C)

    #print(q_treks.shape)
    #print(treks.shape)
q_treks['score'] = q_treks.apply(weighted_rating, axis=1)
q_treks = q_treks.sort_values('score', ascending=False)

def recommenFetch():
    #print(q_treks.head(20))
    dic={'image':q_treks.head(5)['image'].tolist(),'id':q_treks.head(5)['id'].tolist(),'name':q_treks.head(5)['name'].tolist()}
    #print(dict)
    return dic



    
