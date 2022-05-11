import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
@st.cache
def top_n_movies_user_based(user_id, movies: pd.DataFrame, ratings: pd.DataFrame, n_movies: int = 5):
    
    sparse_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    #sample_distance = pd.DataFrame(cosine_distances(sparse_matrix.fillna(0)), columns=sparse_matrix.index, index=sparse_matrix.index)
    
    return cosine_similarity(sparse_matrix.fillna(0))