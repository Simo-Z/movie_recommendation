import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
@st.cache
def top_n_movies_user_based(user_id, movies: pd.DataFrame, ratings: pd.DataFrame, n_movies: int = 5):
    
    sparse_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    # Get User similarity
    user_sim_matrix =cosine_similarity(sparse_matrix.fillna(0))[user_id]
    # weight user ratings
    ratings
    # get most popular 

    # Remove movies that User already saw
    
    return user_sim_matrix